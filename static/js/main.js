/* static/js/home.js */
$(document).ready(function() {
    function loadStats() {
        $.get('/api/get-stats', function(data) {
            $('#totalReports').text(data.total_reports);
            $('#recentReports').text(data.recent_reports);
            $('#locationsCount').text(data.locations_count);
            
            // Update report types
            const reportTypes = $('#reportTypes');
            reportTypes.empty();
            
            Object.entries(data.reports_by_type).forEach(([type, count]) => {
                const percentage = (count / data.total_reports * 100).toFixed(1);
                reportTypes.append(`
                    <div class="mb-4">
                        <div class="flex justify-between mb-1">
                            <span class="text-gray-700 capitalize">${type}</span>
                            <span class="text-gray-600">${count} reports</span>
                        </div>
                        <div class="w-full bg-gray-200 rounded-full h-2">
                            <div class="bg-blue-600 h-2 rounded-full" style="width: ${percentage}%"></div>
                        </div>
                    </div>
                `);
            });
        });
    }

    function loadRecentReports() {
        $.get('/api/get-recent-reports', function(reports) {
            const reportsList = $('#recentReportsList');
            reportsList.empty();

            reports.forEach(report => {
                const date = new Date(report.created_at).toLocaleDateString();
                reportsList.append(`
                    <div class="border-b border-gray-200 pb-6">
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="font-semibold text-lg">${report.incident_type}</h3>
                                <p class="text-gray-600 mt-1">${report.description}</p>
                                ${report.has_evidence ? '<span class="text-blue-600 text-sm">Evidence attached</span>' : ''}
                            </div>
                            <span class="text-sm text-gray-500">${date}</span>
                        </div>
                    </div>
                `);
            });
        });
    }

    // Initial load
    loadStats();
    loadRecentReports();

    // Refresh data periodically
    setInterval(loadStats, 300000); // Every 5 minutes
    setInterval(loadRecentReports, 300000);
});

/* static/js/report.js */
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

    // Try to get user's location
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            map.setView([lat, lng], 13);
        });
    }

    // Handle form submission
    $('#reportForm').on('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        
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
            }
        });
    });
});