const API_URL = "http://127.0.0.1:8000";

async function loadHealth() {
    try {
        const response = await fetch(`${API_URL}/health`);
        const data = await response.json();

        document.getElementById("status").textContent =
            data.status || "Backend connected";
    } catch (error) {
        document.getElementById("status").textContent =
            "Backend unavailable";
    }
}

async function loadTelemetry() {
    try {
        const response = await fetch(`${API_URL}/telemetry`);
        const data = await response.json();

        document.getElementById("cpu").textContent =
            `${data.cpu_usage}%`;

        document.getElementById("memory").textContent =
            `${data.memory_usage}%`;

        document.getElementById("available").textContent =
            `${data.memory_available_gb} GB`;

        document.getElementById("stream").textContent =
            data.stream_status;
    } catch (error) {
        console.error("Telemetry error:", error);
    }
}

loadHealth();
loadTelemetry();

setInterval(loadTelemetry, 5000);