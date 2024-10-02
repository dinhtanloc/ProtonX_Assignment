import streamlit as st
import requests

# Base URL for the API
BASE_URL = "http://localhost:5002/cats"

# Default image link placeholder
DEFAULT_IMAGE_LINK = "https://storage.googleapis.com/mle-courses-prod/users/61b6fa1ba83a7e37c8309756/private-files/3f3d9a50-66aa-11ef-b0a7-998b84b38d43-cat.png"

# Function to fetch all cats (GET ALL)
def get_all_cats():
    response = requests.get(BASE_URL)
    return response.json()

# Function to create a new cat (POST)
def create_cat(name, age, image_link):
    new_cat = {'name': name, 'age': age, 'image_link': image_link}
    response = requests.post(BASE_URL, json=new_cat)
    return response.json()

# Function to update an existing cat (PUT)
def update_cat(cat_id, name, age, image_link):
    updated_cat = {'name': name, 'age': age, 'image_link': image_link}
    response = requests.put(f"{BASE_URL}/{cat_id}", json=updated_cat)
    return response.json()

# Function to delete a cat by ID (DELETE)
def delete_cat(cat_id):
    response = requests.delete(f"{BASE_URL}/{cat_id}")
    return response.status_code

# Streamlit App
st.title("Cat Management API Demo")

# Section to GET all cats
# Section to GET all cats
st.header("GET ALL Cats")
if st.button("Fetch All Cats"):
    cats = get_all_cats()
    cat_ids = list(cats.keys())

    if cat_ids:
        # Display cats in a grid
        cols = st.columns(3)  # 3 cats per row
        for idx, cat_id in enumerate(cat_ids):
            cat = cats[cat_id]
            with cols[idx % 3]:
                # Use default image if the image link is missing or invalid
                image_link = cat.get('image_link', DEFAULT_IMAGE_LINK)
                st.image(image_link or DEFAULT_IMAGE_LINK, width=150)
                st.text(f"Name: {cat['name']}")
                st.text(f"Age: {cat['age']}")
                st.text(f"ID: {cat['id']}")
                


# Divide POST, PUT, and DELETE into three columns
col1, col2, col3 = st.columns(3)

# Column 1: POST a new cat
with col1:
    st.header("POST a New Cat")
    with st.form("Create Cat"):
        new_name = st.text_input("Name")
        new_age = st.number_input("Age", min_value=0, max_value=30, value=1)
        new_image_link = st.text_input("Image Link", placeholder=DEFAULT_IMAGE_LINK)
        submitted = st.form_submit_button("Create Cat")
        if submitted:
            new_cat = create_cat(new_name, new_age, new_image_link)
            st.write("Created Cat:", new_cat)

# Column 2: PUT (Update) a cat
with col2:
    st.header("PUT (Update) a Cat")
    with st.form("Update Cat"):
        update_id = st.text_input("Cat ID to Update (e.g., cat1)")
        update_name = st.text_input("New Name")
        update_age = st.number_input("New Age", min_value=0, max_value=30, value=1)
        update_image_link = st.text_input("New Image Link", placeholder=DEFAULT_IMAGE_LINK)
        submitted = st.form_submit_button("Update Cat")
        if submitted:
            updated_cat = update_cat(update_id, update_name, update_age, update_image_link)
            st.write("Updated Cat:", updated_cat)

# Column 3: DELETE a cat
with col3:
    st.header("DELETE a Cat")
    with st.form("Delete Cat"):
        delete_id = st.text_input("Cat ID to Delete (e.g., cat1)")
        submitted = st.form_submit_button("Delete Cat")
        if submitted:
            status_code = delete_cat(delete_id)
            if status_code == 204:
                st.write(f"Deleted Cat with ID: {delete_id}")
            else:
                st.write("Failed to delete cat. Please check the ID and try again.")

# Running the app
if __name__ == "__main__":
    st._is_running_with_streamlit = True
