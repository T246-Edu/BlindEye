import cloudinary
import cloudinary.uploader


def upload(img):
    cloudinary.config(
        cloud_name="dfehchjmf",
        api_key="529222792259839",
        api_secret="TeyRTj4xxcmHaly7ju_oh9TA7_Y",
        secure=True
    )
    data = cloudinary.uploader.upload(img)
    return data["url"]
