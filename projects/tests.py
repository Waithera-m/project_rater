from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileModelTests(TestCase):
    """
    class supports the creation of tests to test model behavior
    """
    def setUp(self):
        """
        method defines the object to be created before each test
        """
        self.user = User(username='peaches', first_name='name', last_name='other', email='something@something.com', password='somePassword')
        self.user.save()
        self.profile = Profile(user=self.user, bio='something boring', location='Fiji', profile_pic='base.jpg')
    
    # def tearDown(self):
    #     """
    #     method returns database to pristine condition after all tests run
    #     """
    #     Profile.objects.all().delete()
    #     User.objects.all().delete()
    
    def test_instance(self):
        """
        method checks if a profile object is initialized properly
        """
        self.assertTrue(isinstance(self.profile, Profile))
    
    def test_save_profile(self):
        """
        method tests if added profile is saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    # def test_update_profile(self):
    #     """
    #     method test if one can update a profile
    #     """
    #     profile = Profile.objects.create(user=self.user, bio='something boring', location='Fiji', profile_pic='base.jpg')
    #     Profile.objects.filter(id=profile.id).update(bio='a tad bit interesting')
    #     profile.update_profile()
    #     self.assertEqual(profile.bio, 'a tad bit interesting')

    def test_delete_profile(self):
        """
        method tests delete class method
        """
        useruno = User(username='peachesaf', first_name='name2', last_name='other3', email='something11@something.com', password='somePassword')
        self.user.save()
        profile = Profile.objects.create(user=useruno, bio='something frustrating', location='Fiji', profile_pic='base.jpg')
        Profile.objects.filter(pk=profile.pk).delete()
        profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
