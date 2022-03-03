from django.http import HttpRequest
from django.test import SimpleTestCase  # No database is used in this project therefore, SimpleTestCase is used
from django.urls import reverse
from . import views

class HomePageTests(SimpleTestCase):

#1. here, we test that homepage exists and returns a 200 HTTP status code.-assertEquals()	
	def test_home_status_code(self):
		response=self.client.get('/home/')
		self.assertEquals(response.status_code,200)

# 2.Here, We test that it uses home url.-assertEquals()
	def test_view_url_name(self):
		response=self.client.get(reverse('home'))
		self.assertEquals(response.status_code,200)

# 3. here, we test that app uses correct template or not- assertTemplateUsed()
	def test_correct_template_used(self):
		response=self.client.get(reverse('home'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'home.html')
		# self.assertTemplateUsed(response,'about.html')

# 4. here, we test that Page contains correct html - assertContains()
	def test_correct_html(self):
		response=self.client.get('/home/')
		self.assertContains(response,'<h2> Home Page</h2>')

# 5. here , we tests that page does not contain incorrect html- assertNotContains()
	def test_check_incorrect_html(self):
		response=self.client.get('/home/')
		self.assertNotContains(response,'hi...')


class AboutPageTests(SimpleTestCase):

# 6. testing About Page esixts or not
	def test_about_page_status_code(self):
		response=self.client.get('/about/')
		self.assertEquals(response.status_code,200)

# 7. testing it uses about url
	def test_url(self):
		response=self.client.get(reverse('about'))
		self.assertEquals(response.status_code,200)

# 8. testing AboutPageView uses correct template - assertTemplateUsed()
	def test_template(self):
		response=self.client.get(reverse('about'))
		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'about.html')

# 9. testing the About Page Contains correct html 
	def test_html(self):
		response=self.client.get('/about/')
		self.assertContains(response,'<h2> About Us</h2>')

# 10. testing that page does not contain incorrect html - assertNotContains()
	def test_incorrect_html(self):
		response=self.client.get('/about/')
		self.assertNotContains(response,'hi')