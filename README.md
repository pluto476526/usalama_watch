# 🚨 Usalama Watch - Community Safety Platform

*A Django-powered web application for crowdsourced safety information and community protection in Kenya.*

![Usalama Watch](https://img.shields.io/badge/Usalama-Watch-brightgreen) ![Django](https://img.shields.io/badge/Django-4.2-green) ![Python](https://img.shields.io/badge/Python-3.9-blue)

## 🌟 Project Name: **Usalama Watch**

**Usalama** (Swahili for "Safety") + **Watch** (Vigilance/Monitoring)  
*Pronunciation: Oo-sah-lah-mah Watch*

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

**Usalama Watch** is a community-driven safety platform that empowers Kenyan citizens to report, track, and stay informed about safety incidents in their neighborhoods. By crowdsourcing real-time safety information, we create a more transparent and responsive safety ecosystem.

### 🎯 Core Problem Statement
- Crime data is often inaccessible or delayed
- Citizens lack real-time safety information about their areas
- Reporting incidents to authorities can be intimidating or inefficient
- No centralized platform for community safety awareness

### ✨ Our Solution
- **Real-time incident reporting** with anonymous options
- **Interactive safety heat maps** showing area safety trends
- **Emergency services directory** with direct access
- **Police accountability** through community feedback
- **Safety alerts** and neighborhood watch features

## 🚀 Features

### 🔥 Core Features
1. **Anonymous Incident Reporting**
   - Report crimes, accidents, hazards, and police checkpoints
   - Optional media upload (blurred faces automatically)
   - Categorized incident types with severity levels

2. **Live Safety Heat Map**
   - Color-coded safety zones (Green/Yellow/Red)
   - Real-time incident clustering
   - Historical data trends and patterns

3. **Emergency Services Directory**
   - Geolocated police stations, hospitals, fire departments
   - Direct calling integration
   - Service ratings and reviews

4. **Community Alerts**
   - SMS/Email notifications for nearby incidents
   - Neighborhood watch groups
   - Safety tips and preventive information

5. **Police Interaction Reporting**
   - Report positive/negative police encounters
   - Build accountability through transparency
   - Highlight exemplary officers

### 🎨 Advanced Features
- **USSD Integration** for feature phone users
- **Multi-language Support** (English & Swahili)
- **Offline Reporting** capability
- **Data Verification System** to prevent abuse
- **Admin Dashboard** for moderation and analytics

## 🛠 Technology Stack

### Backend
- **Framework**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL with PostGIS extension
- **Authentication**: Django Allauth + JWT tokens
- **Task Queue**: Celery + Redis
- **File Storage**: AWS S3 or Google Cloud Storage

### Frontend
- **Maps**: OpenStreetMap
- **UI Framework**: Bootstrap 5 + Custom CSS
- **Charts**: Plotly Python for analytics
- **Notifications**: Web Push API + Twilio SMS

### DevOps & APIs
- **SMS Integration**: Africa's Talking API
- **Geocoding**: Google Maps Geocoding API
- **Deployment**: Docker + Nginx + Daphne
- **Monitoring**: Sentry + Django Debug Toolbar

## 💻 Installation

### Prerequisites
- Python 3.9+
- PostgreSQL 12+ with PostGIS
- Redis Server
- Git

### 🛠 Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-username/usalama-watch.git
cd usalama-watch
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment configuration**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Database setup**
```bash
# Enable PostGIS in PostgreSQL
createdb usalama_watch
psql -d usalama_watch -c "CREATE EXTENSION postgis;"

# Run migrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Load initial data**
```bash
python manage.py loaddata emergency_services
python manage.py loaddata incident_categories
```

8. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the application!

## 🗃 Database Schema

### Core Models

```python
# incidents/models.py
class Incident(models.Model):
    INCIDENT_TYPES = (
        ('crime', 'Criminal Activity'),
        ('accident', 'Road Accident'),
        ('hazard', 'Public Hazard'),
        ('checkpoint', 'Police Checkpoint'),
        ('other', 'Other Incident'),
    )
    
    SEVERITY_LEVELS = (
        ('low', 'Low Risk'),
        ('medium', 'Medium Risk'),
        ('high', 'High Risk'),
        ('critical', 'Critical Emergency'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY_LEVELS)
    location = models.PointField()  # PostGIS field
    address = models.CharField(max_length=500)
    anonymous = models.BooleanField(default=True)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    verified = models.BooleanField(default=False)
    media_files = models.FileField(upload_to='incident_media/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmergencyService(models.Model):
    SERVICE_TYPES = (
        ('police', 'Police Station'),
        ('hospital', 'Hospital'),
        ('fire', 'Fire Station'),
        ('ambulance', 'Ambulance Service'),
    )
    
    name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    location = models.PointField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)

class PoliceInteraction(models.Model):
    INTERACTION_TYPES = (
        ('positive', 'Positive Interaction'),
        ('negative', 'Negative Interaction'),
        ('neutral', 'Neutral Interaction'),
    )
    
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES)
    description = models.TextField()
    location = models.PointField()
    officer_badge = models.CharField(max_length=50, blank=True)  # Optional
    station = models.CharField(max_length=200)
    anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

## 🌐 API Endpoints

### Public Endpoints
```
GET     /api/incidents/                 # List incidents with filters
POST    /api/incidents/                 # Create new incident (anonymous)
GET     /api/emergency-services/        # List emergency services
GET     /api/safety-stats/              # Safety statistics
```

### Authenticated Endpoints
```
POST    /api/police-interactions/       # Report police interaction
GET     /api/my-reports/               # User's reported incidents
POST    /api/verify-incident/          # Verify incidents (trusted users)
```

### USSD Endpoints
```
POST    /api/ussd/                     # USSD menu handler
```

## 📱 USSD Integration

```python
# USSD menu structure
def handle_ussd_request(phone_number, session_id, service_code, text):
    """
    Sample USSD Flow:
    1. Main Menu: Welcome to Usalama Watch
       1. Report Incident
       2. View Area Safety
       3. Emergency Contacts
       4. Safety Tips
    """
```

## 🎨 Screenshots

*(Placeholder)*

| Homepage with Heat Map | Incident Reporting | Mobile View |
|------------------------|-------------------|-------------|
| ![Homepage]() | ![Reporting]() | ![Mobile]() |

## 🤝 Contributing

We welcome contributions from the community! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 🐛 Issue Reporting
Please use the [GitHub Issues](https://github.com/your-username/usalama-watch/issues) page to report bugs or suggest features.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡️ Privacy & Security

- All anonymous reports are strictly confidential
- Location data is aggregated and anonymized for heat maps
- User data is never sold to third parties
- Compliance with Kenya's Data Protection Act

## 📞 Support

- **Email**: support@usalamawatch.co.ke
- **Twitter**: [@UsalamaWatchKE](https://twitter.com/UsalamaWatchKE)
- **Documentation**: [docs.usalamawatch.co.ke](https://docs.usalamawatch.co.ke)

## 🙏 Acknowledgments

- Kenya Police Service for partnership opportunities
- OpenStreetMap for mapping data
- Africa's Talking for SMS/USSD integration
- The Kenyan developer community

---

**Built with ❤️ for a safer Kenya**

*Usalama Watch - Your Community, Your Safety, Your Voice*
