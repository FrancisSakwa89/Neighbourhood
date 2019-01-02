from django.test import TestCase
from .models import Profile, Neighbourhood, Business

# Create your tests here.
class ProfileTestClass(TestCase):
  """  
  Tests Profile class and its functions
  """

  def test_save_method(self):
      """
      Function to test that profile is being saved
      """

class NeighbourhoodTestClass(TestCase):
  """  
  Tests Neighbourhood class and its functions
  """
  def setUp(self):
      self.hood = Neighbourhood(name='test',location='test',occupants_count=0)

  def test_instance(self):
      self.assertTrue(isinstance(self.hood, Neighbourhood))

  def test_save_method(self):
      """
      Function to test that a neighbourhood is being saved
      """
      self.hood.save_neighbourhood()
      hoods = Neighbourhood.objects.all()
      self.assertTrue(len(hoods) > 0)

  def test_delete_method(self):
      """
      Function to test that a neighbourhood can be deleted
      """
      self.hood.save_neighbourhood()
      self.hood.delete_neighbourhood()
      hoods = Neighbourhood.objects.all()
      self.assertTrue(len(hoods) == 0)



class BusinessTestClass(TestCase):
  """  
  Tests Business Class and its functions
  """
#   
  def test_save_method(self):
      """
      Function to test that a business is being saved
      """
    