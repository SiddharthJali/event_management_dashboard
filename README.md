# Event Management Dashboard

## About the Project
The Event Management Dashboard is a web application designed to streamline the organization and tracking of events, tasks, and attendees. It includes features like event scheduling, task tracking, progress visualization, and attendee management.

### Key Features
- Event tracking and scheduling.
- Task progress visualization using a progress bar.
- Attendee management for task assignment.

---

## Setup Instructions

### Prerequisites
1. Python 3.9 or higher installed on your machine.
2. Virtual environment tool (`venv` or `virtualenv`) installed.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/event-management-dashboard.git
   ```
2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv myenv
   cd event-management-dashboard
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up the Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
  
---

## Developed API

### 1. **List Events**
- **Endpoint**: `GET /events/`
- **Description**: Retrieves a list of all events.
- **Response**:
  ```json
  [
      {
          "id": 1,
          "name": "Annual Meeting",
          "date": "2024-12-25",
          "location": "Conference Hall"
      },
      {
          "id": 2,
          "name": "Team Building Retreat",
          "date": "2024-12-26",
          "location": "Resort"
      }
  ]
  ```

### 2. **Retrieve Event Details**
- **Endpoint**: `GET /events/<id>/`
- **Description**: Retrieves details of a specific event.
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Annual Meeting",
      "date": "2024-12-25",
      "location": "Conference Hall",
      "tasks": [
          {
              "id": 101,
              "name": "Prepare Presentation",
              "status": "Completed"
          },
          {
              "id": 102,
              "name": "Arrange Catering",
              "status": "Pending"
          }
      ]
  }
  ```

### 3. **Create Event**
- **Endpoint**: `POST /events/create/`
- **Description**: Creates a new event.
- **Payload**:
  ```json
  {
      "name": "New Year Party",
      "date": "2024-12-31",
      "location": "Ballroom"
  }
  ```
- **Response**:
  ```json
  {
      "id": 3,
      "name": "New Year Party",
      "date": "2024-12-31",
      "location": "Ballroom"
  }
  ```

### 4. **Update Event**
- **Endpoint**: `PUT/PATCH /events/<id>/edit/`
- **Description**: Updates the details of an existing event.
- **Payload**: Same as the Create Event payload.
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Annual Meeting - Updated",
      "date": "2024-12-25",
      "location": "Main Hall"
  }
  ```

### 5. **Delete Event**
- **Endpoint**: `DELETE /events/<id>/delete/`
- **Description**: Deletes an existing event.
- **Response**:
  ```json
  {
      "message": "Event deleted successfully."
  }
  ```

## Tasks API

### 1. **List Tasks**
- **Endpoint**: `GET /tasks/`
- **Description**: Retrieves a list of all tasks.
- **Response**:
  ```json
  [
      {
          "id": 101,
          "name": "Prepare Presentation",
          "status": "Completed",
          "event_id": 1
      },
      {
          "id": 102,
          "name": "Arrange Catering",
          "status": "Pending",
          "event_id": 1
      }
  ]
  ```

### 2. **Retrieve Task Details**
- **Endpoint**: `GET /tasks/<id>/`
- **Description**: Retrieves details of a specific task.
- **Response**:
  ```json
  {
      "id": 101,
      "name": "Prepare Presentation",
      "status": "Completed",
      "event": {
          "id": 1,
          "name": "Annual Meeting"
      },
      "assigned_to": [
          {
              "id": 5,
              "name": "John Doe"
          }
      ]
  }
  ```

### 3. **Update Task**
- **Endpoint**: `PATCH /tasks/<id>/update/`
- **Description**: Updates the details or status of a specific task.
- **Payload**:
  ```json
  {
      "status": "Completed"
  }
  ```
- **Response**:
  ```json
  {
      "id": 101,
      "name": "Prepare Presentation",
      "status": "Completed"
  }
  ```

## Attendees API

### 1. **List Attendees**
- **Endpoint**: `GET /attendees/`
- **Description**: Retrieves a list of all attendees.
- **Response**:
  ```json
  [
      {
          "id": 5,
          "name": "John Doe",
          "status": "Engaged"
      },
      {
          "id": 6,
          "name": "Jane Smith",
          "status": "Available"
      }
  ]
  ```

### 2. **Assign Task to Attendee**
- **Endpoint**: `POST /attendees/<id>/assign/`
- **Description**: Assigns a task to an attendee.
- **Payload**:
  ```json
  {
      "task_id": 102
  }
  ```
- **Response**:
  ```json
  {
      "message": "Task assigned successfully."
  }
