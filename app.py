# # from flask import Flask, render_template, request, redirect, url_for, flash
# # import requests
# # import os
# # import re

# # app = Flask(__name__)
# # app.secret_key = "welcome to Cliparts"  # required for flash messages

# # # --- API settings ---
# # API_KEY = "vk-x4D2UFTT7sH2FZRac4e3FVh2fPVS0xTCp9Ug9JZzu8qLqchF2"
# # URL = "https://api.vyro.ai/v2/image/generations"
# # out_dir = "Niharika"
# # os.makedirs(out_dir, exist_ok=True)

# # # --- Backend functions ---
# # def clean_filename(text):
# #     text = text.lower()
# #     text = re.sub(r"[^a-z0-9]+", "_", text)
# #     return text.strip("_")

# # def generate_and_save(prompt, idx, style="digital_art", aspect="1:1", seed="8"):
# #     if not prompt.strip():
# #         return None
# #     try:
# #         resp = requests.post(
# #             URL,
# #             headers={"Authorization": f"Bearer {API_KEY}"},
# #             files={
# #                 "prompt": (None, prompt),
# #                 "style": (None, "realistic"),
# #                 "aspect_ratio": (None, aspect),
# #                 "seed": (None, seed),
# #                 "transparent_background": (None, "true")
# #             }
# #         )
# #         if resp.status_code != 200:
# #             print(f"❌ Failed ({resp.status_code}): {resp.text}")
# #             return None

# #         ext = "png"
# #         content_type = resp.headers.get("Content-Type", "").lower()
# #         if "jpeg" in content_type or "jpg" in content_type:
# #             ext = "jpg"

# #         safe_name = clean_filename(prompt)
# #         filename = os.path.join(out_dir, f"{safe_name}.{ext}")

# #         with open(filename, "wb") as f:
# #             f.write(resp.content)
# #         return filename
# #     except Exception as e:
# #         print("❌ Error:", e)
# #         return None

# # # --- Routes ---
# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     if request.method == "POST":
# #         raw_prompts = request.form.get("prompts", "")
# #         prompts = [p.strip() for p in raw_prompts.splitlines() if p.strip()]
# #         if not prompts:
# #             flash("Please enter at least one prompt!")
# #             return redirect(url_for("index"))

# #         generated_files = []
# #         for i, p in enumerate(prompts, start=1):
# #             file_path = generate_and_save(p, i)
# #             if file_path:
# #                 generated_files.append(os.path.basename(file_path))

# #         if generated_files:
# #             flash(f"Generated {len(generated_files)} images! Check 'created_images' folder.")
# #         else:
# #             flash("Failed to generate images. Check console for errors.")
# #         return redirect(url_for("index"))

# #     return render_template("index.html")

# # # --- Run server ---
# # if __name__ == "__main__":
# #     app.run(debug=True, host="0.0.0.0", port=5000)



# # from flask import Flask, render_template, request, redirect, url_for, flash
# # import requests
# # import os
# # import re

# # app = Flask(__name__)
# # app.secret_key = "your_secret_key"

# # API_KEY = "vk-x4D2UFTT7sH2FZRac4e3FVh2fPVS0xTCp9Ug9JZzu8qLqchF2"
# # URL = "https://api.vyro.ai/v2/image/generations"

# # out_dir = "Niharika"
# # os.makedirs(out_dir, exist_ok=True)

# # # --- Backend functions ---
# # def clean_filename(text):
# #     text = text.lower()
# #     text = re.sub(r"[^a-z0-9]+", "_", text)
# #     return text.strip("_")

# # def generate_and_save(prompt, idx, style="digital_art", aspect="1:1"):
# #     if not prompt.strip():
# #         return None
# #     try:
# #         resp = requests.post(
# #             URL,
# #             headers={"Authorization": f"Bearer {API_KEY}"},
# #             files={
# #                 "prompt": (None, prompt),
# #                 "style": (None, "realistic"),
# #                 "aspect_ratio": (None, aspect),
# #                 # "seed": (None, seed),
# #                 "transparent_background": (None, "true")
# #             }
# #         )
# #         if resp.status_code != 200:
# #             print(f"❌ Failed ({resp.status_code}): {resp.text}")
# #             return None

# #         ext = "png"
# #         content_type = resp.headers.get("Content-Type", "").lower()
# #         if "jpeg" in content_type or "jpg" in content_type:
# #             ext = "jpg"

# #         safe_name = clean_filename(prompt)
# #         filename = os.path.join(out_dir, f"{safe_name}.{ext}")

# #         with open(filename, "wb") as f:
# #             f.write(resp.content)
# #         return os.path.basename(filename)
# #     except Exception as e:
# #         print("❌ Error:", e)
# #         return None

# # # --- Routes ---
# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     generated_files = os.listdir(out_dir)
# #     generated_files.sort()  # sort alphabetically

# #     if request.method == "POST":
# #         raw_prompts = request.form.get("prompts", "")
# #         prompts = [p.strip() for p in raw_prompts.splitlines() if p.strip()]
# #         if not prompts:
# #             flash("Please enter at least one prompt!")
# #             return redirect(url_for("index"))

# #         new_files = []
# #         for i, p in enumerate(prompts, start=1):
# #             file_name = generate_and_save(p, i)
# #             if file_name:
# #                 new_files.append(file_name)

# #         if new_files:
# #             flash(f"Generated {len(new_files)} images!")
# #         return redirect(url_for("index"))

# #     return render_template("index.html", images=generated_files)

# # # --- Run Flask ---
# # if __name__ == "__main__":
# #     app.run(debug=True, host="0.0.0.0", port=5000)



# from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
# import requests
# import os
# import re

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# API_KEY = "vk-x4D2UFTT7sH2FZRac4e3FVh2fPVS0xTCp9Ug9JZzu8qLqchF2"
# URL = "https://api.vyro.ai/v2/image/generations"

# out_dir = "Niharika"
# os.makedirs(out_dir, exist_ok=True)

# # --- Backend functions ---
# def clean_filename(text):
#     text = text.lower()
#     text = re.sub(r"[^a-z0-9]+", "_", text)
#     return text.strip("_")

# def generate_and_save(prompt, idx, style="digital_art", aspect="1:1"):
#     if not prompt.strip():
#         return None
#     try:
#         resp = requests.post(
#             URL,
#             headers={"Authorization": f"Bearer {API_KEY}"},
#             files={
#                 "prompt": (None, prompt),
#                 "style": (None, "realistic"),
#                 "aspect_ratio": (None, aspect),
#                 # "seed": (None, seed),
#                 "transparent_background": (None, "true")
#             }
#         )
#         if resp.status_code != 200:
#             print(f"❌ Failed ({resp.status_code}): {resp.text}")
#             return None

#         ext = "png"
#         content_type = resp.headers.get("Content-Type", "").lower()
#         if "jpeg" in content_type or "jpg" in content_type:
#             ext = "jpg"

#         safe_name = clean_filename(prompt)
#         filename = os.path.join(out_dir, f"{safe_name}_{idx}.{ext}")

#         with open(filename, "wb") as f:
#             f.write(resp.content)
#         return os.path.basename(filename)
#     except Exception as e:
#         print("❌ Error:", e)
#         return None

# # --- Route to serve generated images ---
# @app.route('/created_images/<filename>')
# def serve_image(filename):
#     return send_from_directory(out_dir, filename)

# # --- Routes ---
# @app.route("/", methods=["GET", "POST"])
# def index():
#     generated_files = []

#     if request.method == "POST":
#         raw_prompts = request.form.get("prompts", "")
#         prompts = [p.strip() for p in raw_prompts.splitlines() if p.strip()]
#         if not prompts:
#             flash("Please enter at least one prompt!")
#             return redirect(url_for("index"))

#         # Generate only the new images
#         for i, p in enumerate(prompts, start=1):
#             file_name = generate_and_save(p, i)
#             if file_name:
#                 generated_files.append(file_name)

#         if generated_files:
#             flash(f"Generated {len(generated_files)} images!")

#     # Pass only the newly generated images to template
#     return render_template("index.html", images=generated_files)
    

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)


from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import os
import re
import glob

app = Flask(__name__)
app.secret_key = "your_secret_key"

API_KEY = "vk-x4D2UFTT7sH2FZRac4e3FVh2fPVS0xTCp9Ug9JZzu8qLqchF2"
URL = "https://api.vyro.ai/v2/image/generations"

out_dir = "Niharika"
os.makedirs(out_dir, exist_ok=True)

# --- Helper functions ---
def clean_filename(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")

def clear_output_folder():
    files = glob.glob(os.path.join(out_dir, "*"))
    for f in files:
        os.remove(f)

def generate_and_save(prompt, idx, style="digital_art", aspect="1:1"):
    if not prompt.strip():
        return None
    try:
        resp = requests.post(
            URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
            files={
                "prompt": (None, prompt),
                "style": (None, "realistic"),
                "aspect_ratio": (None, aspect),
                # "seed": (None, seed),
                "transparent_background": (None, "true")
            }
        )
        if resp.status_code != 200:
            print(f"❌ Failed ({resp.status_code}): {resp.text}")
            return None

        ext = "png"
        content_type = resp.headers.get("Content-Type", "").lower()
        if "jpeg" in content_type or "jpg" in content_type:
            ext = "jpg"

        safe_name = clean_filename(prompt)
        filename = os.path.join(out_dir, f"{safe_name}_{idx}.{ext}")

        with open(filename, "wb") as f:
            f.write(resp.content)
        return os.path.basename(filename)
    except Exception as e:
        print("❌ Error:", e)
        return None

# --- Route to serve images ---
@app.route('/created_images/<filename>')
def serve_image(filename):
    return send_from_directory(out_dir, filename)

# --- API Route ---
@app.route("/generate_image", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt")
    idx = data.get("idx", 1)
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Clear folder only for the first prompt of this batch
    if idx == 1:
        clear_output_folder()

    file_name = generate_and_save(prompt, idx)
    if file_name:
        return jsonify({"filename": file_name})
    return jsonify({"error": "Failed to generate image"}), 500

# --- Main route ---
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)