// var stats_url = "https://free-nba.p.rapidapi.com/stats?seasons=2001&per_page=100&page="
// var players_url = "https://free-nba.p.rapidapi.com/players?per_page=100&page=0"


for (var i = 1; i < 4; i++) {
    var stats_url = "https://free-nba.p.rapidapi.com/stats?seasons=2001&per_page=100&page="  + i
    
    //loop through API endpoint for each page
    d3.json(stats_url, {
        headers: new Headers({
            "x-rapidapi-key": "38bab05df5msh928211553580d9cp181186jsne583ad5bd5cd",
            "x-rapidapi-host": "free-nba.p.rapidapi.com"
    }),
    }).then(data => console.log(data));
};

// d3.json(stats_url, {
//   headers: new Headers({
//     "x-rapidapi-key": "38bab05df5msh928211553580d9cp181186jsne583ad5bd5cd",
// 		"x-rapidapi-host": "free-nba.p.rapidapi.com"
//   }),
// }).then(data => console.log(data));

// found this solution here: https://stackoverflow.com/questions/1575271/range-of-years-in-javascript-for-a-select-box/1575326
// const currentYear = (new Date()).getFullYear();
// const range = (start, stop, step) => Array.from({ length: (stop - start) / step + 1}, (_, i) => start + (i * step));
// console.log(range(currentYear, currentYear - 20, -1));
// const seasons = range(currentYear, currentYear - 20, -1);