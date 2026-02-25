const API_BASE = "http://localhost:8000";

async function getAdvice() {
    const coin = document.getElementById("coinInput").value;
    const resultBox = document.getElementById("result");

    resultBox.textContent = "Loading...";

    try {
        const res = await fetch(`${API_BASE}/advise`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ coin: coin })
        });

        const data = await res.json();
        resultBox.textContent = data.raw || JSON.stringify(data, null, 2);
    } catch (err) {
        resultBox.textContent = "Error: " + err.message;
    }
}

async function getPortfolio() {
    const coins = document.getElementById("portfolioInput").value
        .split(",")
        .map(c => c.trim());

    const resultBox = document.getElementById("result");
    resultBox.textContent = "Analyzing portfolio...";

    try {
        const res = await fetch(`${API_BASE}/portfolio/advice`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ coins: coins })
        });

        const data = await res.json();
        resultBox.textContent = data.raw || JSON.stringify(data, null, 2);
    } catch (err) {
        resultBox.textContent = "Error: " + err.message;
    }
}