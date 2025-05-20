import streamlit as st

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def main():
    st.set_page_config(page_title="Distance Converter", page_icon="🚗")

    st.image("https://cdn-icons-png.flaticon.com/512/854/854894.png", width=80)
    st.title("🚗 Distance Converter")
    st.write("Convert between **Kilometers** and **Miles**.")

    if 'history' not in st.session_state:
        st.session_state.history = []

    option = st.radio(
        "Choose conversion direction: ",
        ('Kilometers to Miles', 'Miles to Kilometers')
    )

    distance = st.number_input("Enter the distance: ", min_value=0.0, format='%.2f')

    col1, col2 = st.columns([1,1])
    with col1:
        convert = st.button('Convert')

    with col2:
        reset = st.button('Reset')

    if reset:
        st.session_state.history.clear()
        st.experimental_rerun()

    if convert:
        if distance < 0:
            st.warning("Distance cannot be negative. Please enter a non-negative value.")
        else:
            if option == 'Kilometers to Miles':
                converted = km_to_miles(distance)
                result = f"{distance} kilometers is equal to {converted:.2f} miles."
            else:
                converted = miles_to_km(distance)
                result = f"{distance} miles is equal to {converted:.2f} kilometers."

            st.success(result)
            st.session_state.history.append(result)

    # --- Display History ---
    if st.session_state.history:
        st.markdown("### 📜 Conversion History")
        for item in st.session_state.history[::-1]:  # Show latest first
            st.info(item)

            
if __name__ == "__main__":
    main()