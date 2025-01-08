{# templates/base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Corruption Reporting Platform{% endblock %}</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="{{ url_for('static', filename='css/leaflet.css')}}">
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="{{ url_for('static', filename='js/leaflet.js') }}"></script>
    {% block extra_head %}{% endblock %}
</head>
<body class="bg-gray-50 min-h-screen flex flex-col">
    <nav class="bg-blue-600 text-white shadow-lg">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <a href="{{ url_for('home') }}" class="text-xl font-bold hover:text-blue-200">
                    Corruption Reporting Platform
                </a>
                <div class="space-x-6">
                    <a href="{{ url_for('home') }}" class="hover:text-blue-200">Home</a>
                    <a href="{{ url_for('report') }}" class="hover:text-blue-200">Report</a>
                    <a href="{{ url_for('map_view') }}" class="hover:text-blue-200">Map</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="flex-grow container mx-auto px-6 py-8">
        {% block content %}{% endblock %}
    </main>

    <footer class="bg-gray-800 text-white mt-auto">
        <div class="container mx-auto px-6 py-4">
            <p class="text-center text-gray-400">
                Report corruption safely and anonymously
            </p>
        </div>
    </footer>

    <div id="notification" class="fixed top-4 right-4 transform translate-x-full transition-transform duration-300"></div>

    <script>
        function showNotification(message, type = 'success') {
            const notification = document.getElementById('notification');
            notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg ${
                type === 'success' ? 'bg-green-500' : 'bg-red-500'
            } text-white transform translate-x-0 transition-transform duration-300`;
            notification.textContent = message;

            setTimeout(() => {
                notification.classList.add('translate-x-full');
            }, 3000);
        }
    </script>

    {% block extra_scripts %}{% endblock %}
</body> #}
{# </html> #}

{# templates/base.html #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Corruption Reporting Platform{% endblock %}</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="{{ url_for('static', filename='js/tailwind.js') }}"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap" rel="stylesheet">
    {# <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/leaflet.css')}}">
    <script src="{{ url_for('static', filename='js/leaflet.js') }}"></script> #}
    
    {# <s<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css"> #}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/custom.css') }}">
    {% block extra_head %}{% endblock %}
</head>
<body class="bg-gray-900 text-gray-100 min-h-screen flex flex-col dark-theme">
    <nav class="gradient-dark shadow-lg border-b border-gray-800">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <a href="{{ url_for('home') }}" class="flex items-center space-x-3">
                    <svg class="w-8 h-8 text-blue-500" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2L1 21h22L12 2zm0 3.99L19.53 19H4.47L12 5.99zM11 16h2v2h-2zm0-6h2v4h-2z"/>
                    </svg>
                    <span class="caveat-font text-2xl font-bold text-blue-500 hover:text-blue-400">
                        Whistleblower
                    </span>
                </a>
                <div class="space-x-6">
                    <a href="{{ url_for('home') }}" class="hover:text-blue-400">Home</a>
                    <a href="{{ url_for('report') }}" class="hover:text-blue-400">Report</a>
                    <a href="{{ url_for('view_reports') }}" class="hover:text-blue-400">View Reports</a>
                    <a href="{{ url_for('map_view') }}" class="hover:text-blue-400">Map</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="flex-grow container mx-auto px-6 py-8">
        {% block content %}{% endblock %}
    </main>

    <footer class="gradient-dark text-white mt-auto border-t border-gray-800">
        <div class="container mx-auto px-6 py-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <h3 class="caveat-font text-xl font-bold text-blue-500 mb-4">Whistleblower</h3>
                    <p class="text-gray-400">Empowering citizens to fight corruption through anonymous reporting.</p>
                </div>
                <div>
                    <h3 class="font-semibold text-lg mb-4">Quick Links</h3>
                    <ul class="space-y-2 text-gray-400">
                        <li><a href="{{ url_for('home') }}" class="hover:text-blue-400">Home</a></li>
                        <li><a href="{{ url_for('report') }}" class="hover:text-blue-400">Report Corruption</a></li>
                        <li><a href="{{ url_for('view_reports') }}" class="hover:text-blue-400">View Reports</a></li>
                        <li><a href="{{ url_for('map_view') }}" class="hover:text-blue-400">View Map</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-semibold text-lg mb-4">Contact</h3>
                    <ul class="space-y-2 text-gray-400">
                        <li>Emergency Hotline: 0800-CORRUPT</li>
                        <li>Email: report@whistleblower.org</li>
                        <li>Available 24/7</li>
                    </ul>
                </div>
            </div>
            <div class="mt-8 pt-8 border-t border-gray-800 text-center text-gray-400">
                <p>© 2025 Whistleblower. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <div id="notification" class="fixed top-4 right-4 transform translate-x-full transition-transform duration-300"></div>
    <script>
        function showNotification(message, type = 'success') {
            const notification = document.getElementById('notification');
            notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg ${
                type === 'success' ? 'bg-green-500' : 'bg-red-500'
            } text-white transform translate-x-0 transition-transform duration-300`;
            notification.textContent = message;

            setTimeout(() => {
                notification.classList.add('translate-x-full');
            }, 3000);
        }
    </script>

    {% block extra_scripts %}{% endblock %}
</body>
</html>
{# templates/report.html #}
{% extends 'base.html' %}

{% block title %}Submit Report - Whistleblower Platform{% endblock %}

{% block content %}
<div class="max-w-2xl mx-auto">
    <h1 class="caveat-font text-3xl font-bold text-blue-400 mb-8">Submit a Report</h1>
    
    <div class="bg-gray-800 rounded-xl border border-gray-700 p-8">
        <form id="reportForm" class="space-y-6">
            <div>
                <label class="block text-gray-300 font-medium mb-2" for="incidentType">
                    Type of Incident*
                </label>
                <select id="incidentType" name="incident_type" required
                        class="w-full p-3 bg-gray-700 text-white border border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors">
                    <option value="">Select incident type</option>
                    <option value="bribery">Bribery</option>
                    <option value="fraud">Fraud</option>
                    <option value="embezzlement">Embezzlement</option>
                    <option value="other">Other</option>
                </select>
                <div class="text-red-500 text-sm mt-1 hidden" id="incidentTypeError"></div>
            </div>
        
            <div>
                <label class="block text-gray-300 font-medium mb-2" for="description">
                    Description*
                </label>
                <div class="relative">
                    <textarea id="description" name="description" rows="5" required
                              class="w-full p-3 bg-gray-700 text-white border border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
                              placeholder="Please provide details about the incident..."></textarea>
                    <div class="absolute bottom-2 right-2 text-sm text-gray-400">
                        <span id="charCount">0</span>/1000
                    </div>
                </div>
                <div class="text-red-500 text-sm mt-1 hidden" id="descriptionError"></div>
            </div>

            <div>
                <label class="block text-gray-300 font-medium mb-2">
                    Location*
                </label>
                <div id="map" class="h-64 rounded-lg mb-2 border border-gray-600"></div>
                <input type="hidden" id="latitude" name="latitude" required>
                <input type="hidden" id="longitude" name="longitude" required>
                <p class="text-sm text-gray-400">Click on the map to set the location</p>
            </div>

            <!-- Enhanced file upload section -->
    <div class="relative">
        <label class="block text-gray-300 font-medium mb-2" for="evidence">
            Evidence Files
        </label>
        <div class="border-2 border-dashed border-gray-600 rounded-lg p-4 text-center hover:border-blue-500 transition-colors">
            <input type="file" id="evidence" name="evidence" multiple accept=".jpg,.jpeg,.png,.pdf,.mp3,.mp4"
                   class="hidden">
            <label for="evidence" class="cursor-pointer">
                <div class="space-y-2">
                    <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                        <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                    <div class="text-gray-400">
                        Drag and drop files here or click to select
                    </div>
                </div>
            </label>
        </div>
        <div id="fileList" class="mt-4 space-y-2"></div>
    </div>
    

            <div class="flex justify-end">
                <button type="submit"
                        class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
                    Submit Report
                </button>
            </div>
        </form>
    </div>
</div>

{% block extra_scripts %}
<script>
    // Initialize AOS
    document.addEventListener('DOMContentLoaded', function() {
        AOS.init({
            duration: 1000,
            once: true
        });
    });
$(document).ready(function() {
    // Initialize map
    const map = L.map('map').setView([0, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    let marker;
    
    map.on('click', function(e) {
        const lat = e.latlng.lat;
        const lng = e.latlng.lng;
        
        $('#latitude').val(lat);
        $('#longitude').val(lng);
        
        if (marker) {
            marker.setLatLng(e.latlng);
        } else {
            marker = L.marker(e.latlng).addTo(map);
        }
    });

    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            map.setView([lat, lng], 13);
        });
    }
 // Enhanced form validation
 const form = document.getElementById('reportForm');
 const description = document.getElementById('description');
 const charCount = document.getElementById('charCount');
 const fileInput = document.getElementById('evidence');
 const fileList = document.getElementById('fileList');

 // Character counter
 description.addEventListener('input', function() {
     const count = this.value.length;
     charCount.textContent = count;
     if (count > 1000) {
         this.value = this.value.slice(0, 1000);
         charCount.textContent = 1000;
     }
 });

 // File upload preview
 fileInput.addEventListener('change', function(e) {
     fileList.innerHTML = '';
     Array.from(this.files).forEach(file => {
         const div = document.createElement('div');
         div.className = 'flex items-center justify-between bg-gray-700 p-2 rounded';
         div.innerHTML = `
             <span class="text-gray-300">${file.name} (${(file.size / 1024 / 1024).toFixed(2)} MB)</span>
             <button type="button" class="text-red-500 hover:text-red-400">Remove</button>
         `;
         div.querySelector('button').onclick = () => {
             div.remove();
             // Need to handle file removal from input
         };
         fileList.appendChild(div);
     });
 });

 // Drag and drop
 const dropZone = document.querySelector('.border-dashed');
 ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
     dropZone.addEventListener(eventName, preventDefaults, false);
 });

 function preventDefaults (e) {
     e.preventDefault();
     e.stopPropagation();
 }

 ['dragenter', 'dragover'].forEach(eventName => {
     dropZone.addEventListener(eventName, highlight, false);
 });

 ['dragleave', 'drop'].forEach(eventName => {
     dropZone.addEventListener(eventName, unhighlight, false);
 });

 function highlight(e) {
     dropZone.classList.add('border-blue-500', 'bg-blue-500', 'bg-opacity-10');
 }

 function unhighlight(e) {
     dropZone.classList.remove('border-blue-500', 'bg-blue-500', 'bg-opacity-10');
 }

 dropZone.addEventListener('drop', handleDrop, false);

 function handleDrop(e) {
     const dt = e.dataTransfer;
     const files = dt.files;
     fileInput.files = files;
     const event = new Event('change');
     fileInput.dispatchEvent(event);
 }

 // Form validation
 form.addEventListener('submit', function(e) {
     e.preventDefault();
     let isValid = true;
     
     // Reset errors
     document.querySelectorAll('.text-red-500').forEach(el => el.classList.add('hidden'));
     
     // Validate incident type
     const incidentType = document.getElementById('incidentType');
     if (!incidentType.value) {
         document.getElementById('incidentTypeError').textContent = 'Please select an incident type';
         document.getElementById('incidentTypeError').classList.remove('hidden');
         isValid = false;
     }
     
     // Validate description
     if (!description.value || description.value.length < 50) {
         document.getElementById('descriptionError').textContent = 'Please provide a detailed description (minimum 50 characters)';
         document.getElementById('descriptionError').classList.remove('hidden');
         isValid = false;
     }
     
     // Validate location
     const lat = document.getElementById('latitude');
     const lng = document.getElementById('longitude');
     if (!lat.value || !lng.value) {
         showNotification('Please select a location on the map', 'error');
         isValid = false;
     }
     
     if (isValid) {
         // Submit form
         const formData = new FormData(this);
         submitReport(formData);
     }
 });

 function submitReport(formData) {
     const submitButton = form.querySelector('button[type="submit"]');
     submitButton.disabled = true;
     submitButton.innerHTML = '<span class="inline-block animate-spin mr-2">↻</span> Submitting...';
     
     $.ajax({
         url: '/api/submit-report',
         type: 'POST',
         data: formData,
         processData: false,
         contentType: false,
         success: function(response) {
             showNotification('Report submitted successfully', 'success');
             setTimeout(() => {
                 window.location.href = '/';
             }, 2000);
         },
         error: function(xhr) {
             const message = xhr.responseJSON?.message || 'An error occurred';
             showNotification(message, 'error');
             submitButton.disabled = false;
             submitButton.textContent = 'Submit Report';
         }
     });
    }
});
</script>
{% endblock %}
{% endblock %}
/* custom.css */

.caveat-font {
    font-family: 'Caveat', cursive;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4); }
    70% { box-shadow: 0 0 0 10px rgba(59, 130, 246, 0); }
    100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
}

.float-animation {
    animation: float 3s ease-in-out infinite;
}

.pulse-animation {
    animation: pulse 2s infinite;
}

.gradient-text {
    background: linear-gradient(45deg, #3B82F6, #10B981);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hover-card {
    transition: all 0.3s ease;
}

.hover-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

/* New color scheme */
:root {
    --primary-blue: #3B82F6;
    --accent-yellow: #FBBF24;
    --accent-orange: #F97316;
    --accent-green: #10B981;
    --hover-blue: #2563EB;
}