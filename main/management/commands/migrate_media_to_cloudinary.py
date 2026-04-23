from django.core.management.base import BaseCommand
from django.apps import apps
import cloudinary.uploader


class Command(BaseCommand):
    help = "Upload all media files to Cloudinary"

    def handle(self, *args, **kwargs):

        self.stdout.write("🚀 Starting Cloudinary migration...")

        models_with_images = [
            "CompanyInfo",
            "TeamPage",
            "Employee",
            "AboutPage",
            "ServicesPage",
            "ServiceArea",
            "BlogPage",
            "BlogPost",
            "Karier",
        ]

        uploaded_count = 0

        for model_name in models_with_images:
            model = apps.get_model("main", model_name)

            for obj in model.objects.all():

                for field in obj._meta.fields:

                    if field.get_internal_type() == "ImageField":

                        file_field = getattr(obj, field.name)

                        if not file_field:
                            continue

                        # ❌ تجاهل الصور الافتراضية
                        if not file_field.name:
                            continue

                        try:
                            file_field.open()

                            result = cloudinary.uploader.upload(file_field.file)

                            setattr(obj, field.name, result["public_id"])

                            uploaded_count += 1
                            self.stdout.write(f"✔ Uploaded: {file_field.name}")

                        except Exception as e:
                            self.stdout.write(f"❌ Failed: {file_field.name} -> {e}")

        self.stdout.write(
            self.style.SUCCESS(f"🎉 Migration finished. Total uploaded: {uploaded_count}")
        )