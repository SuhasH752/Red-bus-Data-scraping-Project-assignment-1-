{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cdf74509-ec3f-4086-b5ad-8551f818358a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-07-31 13:58:42.631 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\suhas\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import mysql.connector\n",
    "\n",
    "\n",
    "# Database connection\n",
    "db_config = {\n",
    "    'host': 'localhost',\n",
    "    'user': 'root',\n",
    "    'password': '12345678',\n",
    "    'database': 'redbus'\n",
    "}\n",
    "\n",
    "try:\n",
    "    conn = mysql.connector.connect(**db_config)\n",
    "    st.success(\"Connected to the database!\")\n",
    "except mysql.connector.Error as err:\n",
    "    st.error(f\"Error: {err}\")\n",
    "\n",
    "# Title of the webpage\n",
    "st.title('Bus Ticket Booking System')\n",
    "\n",
    "# Dropdowns for user input\n",
    "route = st.selectbox('Select the Route', ['Hyderabad to Delhi', 'Delhi to Hyderabad', '...'])\n",
    "bus_type = st.selectbox('Select Bus Type', ['Sleeper', 'Seater'])\n",
    "ac_type = st.selectbox('Select AC Type', ['AC', 'Non-AC'])\n",
    "bus_fare = st.selectbox('Select Bus Fare Range', ['300-400', '400-600','600-1000','1000-3000'])\n",
    "star_rating = st.selectbox('Select Star Rating', ['1-2','2-3','3-4','4-5'])\n",
    "#dept_time = st.selectionbox('Select Dept Time',[\n",
    "\n",
    "\n",
    "# Displaying the table with bus options\n",
    "bus_options = {\n",
    "    'Departure names': ['Hyderabad', 'Delhi'],\n",
    "    'Reaching names': ['Delhi', 'Hyderabad'],\n",
    "    # Add other columns as per your data structure\n",
    "}\n",
    "\n",
    "st.table(bus_options)\n",
    "\n",
    "# Additional features (optional):\n",
    "# You can add more widgets, buttons, or interactive elements here.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a3e591e-b608-4edd-9e34-ab3dba223dd7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4b3930f-6189-4288-996f-881f143ec9c8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8f9194b-de5a-49cc-bf24-8842881f697d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
