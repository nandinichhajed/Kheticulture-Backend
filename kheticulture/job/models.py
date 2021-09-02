from django.db import models
from orders.models import Order
from django.utils.translation import gettext_lazy as _

class Job(models.Model):
	
	order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
	job_start_date_time=models.DateTimeField(auto_now_add=True)
	job_end_date_time=models.DateTimeField()
	description=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
	#created = models.DateTimeField(auto_now_add=True)
	
class JobImage(models.Model):
    """
    The Job Image table.
    """

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a job progress image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Job Image")
        verbose_name_plural = _("Job Images")
		
		
class JobVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        
    def __str__(self):
        return self.title
	
	

# Create your models here.
