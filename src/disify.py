from requests import Session

class Disify:
	def __init__(self) -> None:
		self.api = "https://www.disify.com"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def _get(self, endpoint: str) -> dict:
		return self.session.get(f"{self.api}{endpoint}").json()

	def check_email(self, email: str) -> dict:
		return self._get(f"/api/email/{email}")
	
	def check_domain(self, domain: str) -> dict:
		return self._get(f"/api/domain/{domain}")
	
	def view_validation_results(self, session: str) -> dict:
		return self._get(f"/api/view/{session}")
	
	def check_emails(self, emails: str) -> dict:
		return self._get(f"/api/email/{emails}/mass")
	
	def check_domains(self, domains: str) -> dict:
		return self._get(f"/api/domain/{domains}/mass")
