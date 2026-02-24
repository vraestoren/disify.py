from requests import Session

class Disify:
	def __init__(self) -> None:
		self.api = "https://www.disify.com"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def check_email(self, email: str) -> dict:
		return self.session.get(
			f"{self.api}/api/email/{email}").json()
	
	def check_domain(self, domain: str) -> dict:
		return self.session.get(
			f"{self.api}/api/domain/{domain}").json()
	
	def view_validation_results(self, session: str) -> dict:
		return self.session.get(
			f"{self.api}/api/view/{session}").json()
	
	def check_emails(
			self, emails: str) -> dict:
		return self.session.get(
			f"{self.api}/api/email/{emails}/mass").json()
	
	def check_domains(
			self,
			domains: str) -> dict:
		return self.session.get(
			f"{self.api}/api/domain/{domains}/mass").json()
	
	def get_blocked_domains(self) -> str:
		return self.session.get(
			f"{self.api}/blacklist/domains").text
