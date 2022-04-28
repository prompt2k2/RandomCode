// average request duration by name
let start=datetime("2021-11-22T09:32:00.000Z");
let end=datetime("2021-11-23T09:32:00.000Z");
let timeGrain=5m;
let dataset=requests
    // additional filters can be applied here
    | where timestamp > start and timestamp < end
    | where client_Type != "Browser"
;// calculate average request duration for all requests
dataset
| summarize avg(duration) by bin(timestamp, timeGrain)
| extend request='Overall'
// render result in a chart
| render timechart