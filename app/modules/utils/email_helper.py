import os

import resend

import re


class EmailHelper:
    def __init__(self):
        self.api_key = os.environ.get("RESEND_API_KEY")
        self.transaction_emails_enabled = (
            os.environ.get("TRANSACTION_EMAILS_ENABLED", "false").lower() == "true"
        )
        self.from_address = os.environ.get(
            "EMAIL_FROM_ADDRESS", "dhiren@updates.developer_assist_ai.ai"
        )
        resend.api_key = self.api_key

    async def send_email(self, to_address, repo_name, branch_name):
        if not self.transaction_emails_enabled:
            return

        if not to_address:
            return

        params = {
            "from": f"Dhiren Mathur <{self.from_address}>",
            "to": to_address,
            "subject": f"Your repository {repo_name} is ready! 🥧",
            "reply_to": "dhiren@developer_assist_ai.ai",
            "html": f"""
<p>Hi!</p>

<p>Great news! Your repository <strong>{repo_name}</strong> (branch: <strong>{branch_name}</strong>) has been successfully processed.</p>

<p>Ready to get started? You can now chat with your repository using our AI agents at <a href='https://app.developer_assist_ai.ai/newchat?repo={repo_name}&branch={branch_name}'>app.developer_assist_ai.ai</a>.</p>

<p>Check out our <a href='https://docs.developer_assist_ai.ai'>documentation</a> to make the most of Potpie's features.</p>

<p>Have questions? Just reply to this email - we're here to help!</p>

<p>Best,<br />
Dhiren Mathur<br />
Co-Founder, Potpie 🥧</p>

<p>P.S. Love Potpie? Give us a ⭐ on <a href='https://github.com/Potpie-AI/developer_assist_ai/'>GitHub</a>! And don't hesitate to open an issue if you run into any problems.</p>
            """,
        }

        email = resend.Emails.send(params)
        return email


def is_valid_email(email: str) -> bool:
    """Simple regex-based email validation."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None
