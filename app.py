from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Default fallback avatar if user leaves image URL blank or invalid
DEFAULT_AVATAR = "https://ui-avatars.com/api/?background=4f46e5&color=fff&size=200&name="


def sanitize_profile_data(form_data: dict) -> tuple[dict | None, str | None]:
    """
    Validates and formats incoming POST form data for the user profile card.
    Returns (profile_dict, error_message).
    """
    name = form_data.get("name", "").strip()
    role = form_data.get("role", "").strip()
    bio = form_data.get("bio", "").strip()
    image_url = form_data.get("image_url", "").strip()

    if not name or not bio:
        return None, "Name and Bio are required fields to generate a profile card."

    # Provide a clean generated avatar if no custom URL is supplied
    if not image_url:
        formatted_name = name.replace(" ", "+")
        image_url = f"{DEFAULT_AVATAR}{formatted_name}"

    profile = {
        "name": name,
        "role": role if role else "Member",
        "bio": bio,
        "image_url": image_url,
        "generated_at": datetime.now().strftime("%b %d, %Y • %I:%M %p"),
    }
    return profile, None


@app.route("/", methods=["GET", "POST"])
def index():
    profile = None
    error = None

    if request.method == "POST":
        profile, error = sanitize_profile_data(request.form)

    return render_template("index.html", profile=profile, error=error)


if __name__ == "__main__":
    app.run(debug=True)