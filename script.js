

const locationButtons = document.querySelectorAll(".location-btn");

locationButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        const alertItem = button.closest(".alert-item");

        const title = alertItem.querySelector(".alert-title").textContent.trim();

        alert(
            "Location selected:\n\n" + title +
            "\n\nThe location will be displayed on the map."
        );

    });

});




const viewAllButtons = document.querySelectorAll(".view-all-btn");

viewAllButtons.forEach(function (button) {

    button.addEventListener("click", function () {

        alert("Showing all available alerts.");

    });

});




const reportButton = document.querySelector(".report-btn");

reportButton.addEventListener("click", function () {

    alert(
        "Report generation started.\n\n" +
        "This is currently a frontend demonstration."
    );

});




const csvButton = document.querySelector(".csv-btn");

csvButton.addEventListener("click", function () {

    const data = [
        ["Type", "Location (KM)", "Distance", "Confidence"],
        ["Tree", "4.2", "2.3 m", "96%"],
        ["Rock", "8.7", "1.1 m", "91%"],
        ["Debris", "12.1", "3.4 m", "87%"],
        ["Tree", "18.6", "2.7 m", "88%"],
        ["Rock", "22.3", "1.5 m", "93%"],
        ["Debris", "23.7", "2.1 m", "89%"]
    ];


    let csvContent = "";

    data.forEach(function (row) {

        csvContent += row.join(",") + "\n";

    });


    const blob = new Blob(
        [csvContent],
        {
            type: "text/csv;charset=utf-8;"
        }
    );


    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "road-survey-obstacles.csv";

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);

});




const pdfButton = document.querySelector(".pdf-btn");

pdfButton.addEventListener("click", function () {

    alert(
        "PDF download selected.\n\n" +
        "A PDF library/backend can be connected later."
    );

});



const cards = document.querySelectorAll(".stat-card");

cards.forEach(function (card) {

    card.addEventListener("mouseenter", function () {

        card.style.transform = "translateY(-2px)";

        card.style.transition = "0.2s";

    });


    card.addEventListener("mouseleave", function () {

        card.style.transform = "translateY(0)";

    });

});
