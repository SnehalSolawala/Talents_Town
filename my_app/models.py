from django.db import models

# Create your models here.
class Userinfo(models.Model):
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Mobile = models.CharField(max_length = 100)
    EmailId = models.EmailField()
    Password = models.CharField(max_length = 100)
    role = models.CharField(max_length=100,default='user')
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.EmailId 

class Uploadvideo(models.Model):
    user = models.ForeignKey(Userinfo,on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/')
    catagory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    dis = models.TextField()
    likes = models.ManyToManyField(Userinfo, related_name="liked_users")
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.FirstName + ' ' + self.catagory

    def total_likes(self):
        print("##############################",self.likes.count())
        self.like_count = self.likes.count()
        return self.likes.count()

class Notification(models.Model):
    user = models.ForeignKey(Userinfo,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    dis = models.TextField()
    adimage = models.FileField(upload_to='images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email= models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.firstname


class Video_Report(models.Model):
    video = models.ForeignKey(Uploadvideo, on_delete=models.CASCADE)
    user = models.ManyToManyField(Userinfo, related_name="report_users")
    report = models.TextField()

class Like_contact(models.Model):
    user = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    video = models.ForeignKey(Uploadvideo, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.FirstName + '  ----->  ' + self.video.user.FirstName