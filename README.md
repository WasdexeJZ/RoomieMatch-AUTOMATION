# RoomMate Matcher App

This is a Flutter-based mobile application developed as part of the Software Engineering Group Project module at the University of Nottingham Malaysia Campus. The app aims to match users with potential roommates using features inspired by modern dating applications.

## Project Overview

The **RoomMate Matcher App** allows users to:

- Create a profile with personal information and preferences.
- Swipe right to show interest and swipe left to reject a potential match.
- Filter potential matches based on user-defined preferences such as budget, lifestyle habits, and cleanliness.
- Enter a “Do Not Disturb” mode to be excluded from matching once a match is found.
- Leverage a trained recommendation model to improve the quality of matches over time.

## Features Implemented

- User profile creation with preferences.
- Swipe-based matching interface.
- Filtering algorithm based on user preferences.
- UI/UX design improvements including:
  - Streamlined layout and navigation.
  - Refined color scheme.
  - Redesigned bottom navigation bar.
- Functional onboarding flow (welcome, login, homepage).
- Registration flow designed and implemented.

## Features Planned (But Not Included in Final Build)

- Image and video carousel for profile viewing.
- Enhanced swipe screen with dynamic media elements.

## Technologies Used

- **Framework:** Flutter, FastAPI (Backend)
- **IDE:** Visual Studio Code
- **Language:** Dart, Python (Backend)
- **Design Tools:** Figma (for UI drafts and flow design)
- **Database Service:** MySQL
- **Authentication Service:** SuperTokens Authentication Server
- **Notification Service:** NTFY Notification Server

## Frontend Folder Structure

```bash
lib/
├── main.dart # Entry point
├── chat_detail_page.dart # Chat interface
├── filter_page.dart # Filtering preferences
├── info_page.dart # App info
├── style.dart # Global styles and themes
├── models/ # Data models
├── services/ # Backend / logic services
├── stores/ # App state and data storage
└── views/ # UI widgets and layouts
```

---

## 🚀 Getting Started

### Frontend Prerequisites

#### Please refer to official documentation for installation and setup process

- Flutter SDK installed
- Emulator or physical mobile device
- VS Code or Android Studio

### Frontend Installation

```bash
git clone https://github.com/WasdexeJZ/RoomieMatch-FRONTEND.git
cd RoomieMatch-FRONTEND-master
flutter pub get
flutter run
```

### Backend Prerequisites

#### Please refer to official documentation for installation and setup process

- WSL installed
- Docker on WSL installed

### Backend Installation

```bash
git clone https://github.com/WasdexeJZ/RoomieMatch-BACKEND
git clone https://github.com/WasdexeJZ/RoomieMatch-SUPERTOKEN-CORE-MYSQL-AUTH
git clone https://github.com/WasdexeJZ/RoomieMatch-NTFY-SERVER
git clone https://github.com/WasdexeJZ/RoomieMatch-MYSQL-APP
git clone https://github.com/WasdexeJZ/RoomieMatch-AUTOMATION
```

- Convert all outer folder names to all lower case and remove "RoomieMatch-" and "-master"
- Move all folders into the folder named "automation"

```bash
cd automation
```

- In WSL, navigate to "automation"

```bash
docker compose up -d
```

- Navigate to each folder in "automation" and run the above command to build and run the Docker containers

```bash
cd ..
./kill.sh
./import_volume.sh
./run.sh
```

- Navigate back to automation, still in WSL, run the script "./kill.sh" using the command above to kill all Docker containers
- Next, run the "./import_volume.sh" script to import all the zip file backups into the Docker volumes
- Finally, run "./run.sh" script to run all the Docker containers and voilà, the backend is running in your WSL and now you can connect the Frontend to the Backend to start your experience!

```bash
./export_volume.sh
```

- If you wish to backup the volumes, like backing up the database data, you can run the above script "./export_volume.sh" in "automation" folder which would create a copy of the Docker volumes and zip it up in 49mb files and store it back to the respective folder. In each folder, you can connect your GitHub account to the Git and push the backup to your GitHub repo. The limitation of 49mb is done on purpose to enable users to backup their data and push to GitHub as GitHub has a limitation of 100mb files, and 50mb would trigger warnings, hence we have designed to split the zip files into 49mb split zip files.

## 🙌 Acknowledgments

- **Special thanks to:**
- Dr. Yasir Hafeez (Academic Supervisor)
- Joyful Journeys Travel & Vacation Sdn. Bhd. (Client)
