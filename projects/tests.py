from django.test import TestCase
from .models import Profile, Tags, Project
from django.contrib.auth.models import User
import factory
from django.db.models import signals

# Create your tests here.
class ProfileModelTests(TestCase):
    """
    class supports the creation of tests to test model behavior
    """
    @factory.django.mute_signals(signals.pre_save, signals.post_save)

    def setUp(self):
        """
        method defines the object to be created and instructions to be executed before each test
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
    
    def test_update_profile(self):
        """
        method test if one can update a profile
        """
        profile = Profile.objects.create(user=self.user, bio='something boring', location='Fiji', profile_pic='base.jpg')
        Profile.objects.filter(id=profile.id).update(bio='a tad bit interesting')
        profile.update_profile()
        self.assertEqual(profile.bio, 'a tad bit interesting')

    def test_delete_profile(self):
        """
        method tests delete class method
        """
        usertrois = User(username='peachesaf', first_name='name2', last_name='other3', email='something11@something.com', password='somePassword')
        usertrois.save()
        profileuno = Profile.objects.create(user=usertrois, bio='something frustrating', location='Fiji', profile_pic='base.jpg')
        Profile.objects.filter(pk=profileuno.user.pk).delete()
        profileuno.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class TagsModelTests(TestCase):
    """
    class facilitates the creation of unit tests for tags model's behavior
    """
    def setUp(self):
        """
        method defines the properties of tags' objects before each test
        """
        self.tags = Tags(name='animation')
    
    def test_instance(self):
        """
        method checks if a tags object is initialized properly
        """
        self.assertIsInstance(self.tags, Tags)
    
    def test_save_tag(self):
        """
        method checks if an added tag is saved
        """
        self.tags.save_tags()
        tags = Tags.objects.all()
        self.assertTrue(len(tags) > 0)
    
    def test_update_tag(self):
        """
        method check if saved tag can be updated
        """
        self.tags.save_tags()
        Tags.objects.filter(pk=self.tags.pk).update(name='CSS3')
        self.tags.update_tags()
        self.assertEqual(self.tags.name, 'CSS3')
    
    def test_delete_tag(self):
        """
        method checks if saved tag can be deleted
        """
        self.tags.save_tags()
        self.tags.delete_tags()
        tags = Tags.objects.all()
        self.assertTrue(len(tags) == 0)


