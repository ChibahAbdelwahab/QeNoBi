var sankeyChart = echarts.init(document.getElementById('sankeyDiagram'));
let colors_dict = {
    "S": "#457b9d",
    "M": "#e63946",
    "G": "#a8dadc",
    "ST": "#1d3557",
    "P": "#FFFFFF"
}
sankey_links.map(e => {
    e.lineStyle = {
        'color': colors_dict[e.label], 'opacity': 1
    }
    return e
})
console.log(sankey_links)
let sankey = {
    "top": "5%",
    "bottom": "15%",
    "left": "1%",
    "right": "1%",
    "type": "sankey",
    "name": "Sankey",
    "focusNodeAdjacency": "allEdges",
    "nodeAlign": "center",
    "layout": "none",
    "data": sankey_groups,
    "links": sankey_links,
    'label': {
        distance: 0,
        position: "inside",
        formatter: 'G{b}',
    },
}
let sankey_default = JSON.parse(JSON.stringify(sankey))


var data1 = [];
var data2 = [];
var data3 = [];

var random = function (max) {
    return (Math.random() * max).toFixed(3);
};

for (var i = 0; i < 500; i++) {
    data1.push([random(15), random(10), random(1)]);
    data2.push([random(10), random(10), random(1)]);
    data3.push([random(15), random(10), random(1)]);
}

// specify chart configuration item and data
var title = ""
if (customers_properties) {
    title = "Most frequent purchases for Retail customers by " + customers_properties
} else {
    title = "Most frequent purchases for Retail customers"
}
var option = {
    title: {
        text: title,
        textStyle: {
            fontSize: 27,
            top: 20
        },
        left: "3%",
    },
    grid: {
        left: '2%',
        right: '2%',
        top: '30%',
        bottom: '10%',
    },
    legend: {
        opacity: 0.6,
        textStyle: {
            fontSize: 20,
        },
        data: [
            {
                "name": "Stable",
                "lineStyle": {
                    "color": "#457b9d",
                    "opacity": 1
                }
            },

            {
                "name": "Merges",
                "lineStyle": {
                    "color": "#457b9d",
                    "opacity": 1
                }
            },
            {"name": "Splits"},
            {
                "name": "Grows",
                itemStyle: {
                    color: "#a8dadc",
                    "opacity": 1

                }
            },
            {"name": "Perishes"},
        ],
        right: 10,
    },
    xAxis: [
        {
            position: "bottom",
            type: 'category',
            boundaryGap: false,
            nameRotate: 1,
            splitLine: {
                show: false
            },
            data: periods,
        },
        {
            position: "bottom",
            offset: 25,
            zlevel: 1,
            type: 'category',
            boundaryGap: false,
            nameRotate: 2,
            splitLine: {
                show: false
            },
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            data: periods
        }
    ],
    yAxis: {
        show: false,
    },
    dataZoom: {
        start: 0,
        end: 100,

    },
    tooltip: {
        enabled: false,
        align: "bottom",
        itemGap: 1,
        padding: [0, 0, 0, 0],
        formatter: function (x) {
            return null

            if (x.dataType == "node") {
                return "<b>Group id: </b>" + x.data.name +
                    "<br><b>Size: </b>" + x.data.size +
                    "<hr><b>Users: </b>" + x.data.user_ids +
                    "<br><b>Itemset :</b>" + x.data.itemset_name +
                    "<br><b>Period :</b>" + x.data.period
            }
            if (x.dataType == "edge") {
                return "<b>Users: </b>" + x.data.user_id +
                    "<br><b>Count: </b>" + x.data.value +
                    "<br><b>Label: </b>" + x.data.label +
                    "<hr><b>" + x.data.source + "</b>" + "=><b>" + x.data.target
            } else
                return '<b>User_id :</b>' + x.data.user_id + " <br><b>Count :</b>" + x.data.value
        }
    },
    series: [
        {
            name: "Merges",
            type: 'bar',
            itemStyle: {
                color: "#e63946",
            }

        },
        {
            name: "Splits",
            type: 'bar',
            itemStyle: {
                color: "#1d3557",
            }

        },
        {
            name: "Grows",
            type: 'bar',
            itemStyle: {
                color: "#a8dadc",
                "opacity": 1

            }


        },
        {
            name: "Stable",
            type: 'bar',
            itemStyle: {
                color: "#457b9d",
            }

        },
        {
            name: "Perishes",
            type: 'bar',
            itemStyle: {
                color: "#aFFFF",
            }

        },
        {
            "top": "0%",
            "bottom": "-10%",
            "left": "0%",
            "right": "0%",
            type: 'scatter',
        },
        sankey
    ],

};
sankeyChart.setOption(option);


var timeSeries = echarts.init(document.getElementById('timeSeries'));
ts_data = [['2017-03-05', 3],
    ['2017-03-12', 12],
    ['2017-03-19', 17],
    ['2017-03-26', 11],
    ['2017-04-02', 23],
    ['2017-04-09', 21],
    ['2017-04-16', 37],
    ['2017-04-23', 25],
    ['2017-04-30', 18],
    ['2017-05-07', 9],
    ['2017-05-14', 4],
    ['2017-05-21', 8],
    ['2017-05-28', 1],
    ['2017-06-04', 7],
    ['2017-06-11', 7],
    ['2017-06-18', 6],
    ['2017-06-25', 6],
    ['2017-07-02', 3],
    ['2017-07-09', 6],
    ['2017-07-16', 1],
    ['2017-07-23', 2],
    ['2017-07-30', 1],
    ['2017-08-06', 2],
    ['2017-08-13', 2],
    ['2017-08-20', 4],
    ['2017-08-27', 2],
    ['2017-09-03', 7],
    ['2017-09-10', 7],
    ['2017-09-17', 14],
    ['2017-09-24', 8],
    ['2017-10-01', 18],
    ['2017-10-08', 22],
    ['2017-10-15', 30],
    ['2017-10-22', 37],
    ['2017-10-29', 38],
    ['2017-11-05', 24],
    ['2017-11-12', 35],
    ['2017-11-19', 36],
    ['2017-11-26', 32],
    ['2017-12-03', 34],
    ['2017-12-10', 46],
    ['2017-12-17', 34],
    ['2017-12-24', 34],
    ['2017-12-31', 19],
    ['2018-01-07', 18],
    ['2018-01-14', 18],
    ['2018-01-21', 21],
    ['2018-01-28', 18],
    ['2018-02-04', 17],
    ['2018-02-11', 43],
    ['2018-02-18', 66],
    ['2018-02-25', 41],
    ['2018-03-04', 45],
    ['2018-03-11', 33],
    ['2018-03-18', 25],
    ['2018-03-25', 32],
    ['2018-04-01', 15],
    ['2018-04-08', 21],
    ['2018-04-15', 13],
    ['2018-04-22', 8],
    ['2018-04-29', 15],
    ['2018-05-06', 4],
    ['2018-05-13', 3],
    ['2018-05-20', 4],
    ['2018-05-27', 1],
    ['2018-06-03', 5],
    ['2018-06-10', 8],
    ['2018-06-17', 6],
    ['2018-06-24', 3],
    ['2018-07-01', 2],
    ['2018-07-08', 5],
    ['2018-07-15', 6],
    ['2018-07-22', 3],
    ['2018-07-29', 4],
    ['2018-08-05', 7],
    ['2018-08-12', 4],
    ['2018-08-19', 3],
    ['2018-08-26', 3],
    ['2018-09-02', 1],
    ['2018-09-09', 7],
    ['2018-09-16', 8],
    ['2018-09-23', 9],
    ['2018-09-30', 17],
    ['2018-10-07', 20],
    ['2018-10-14', 27],
    ['2018-10-21', 31],
    ['2018-10-28', 25],
    ['2018-11-04', 14],
    ['2018-11-11', 35],
    ['2018-11-18', 39],
    ['2018-11-25', 52],
    ['2018-12-02', 37],
    ['2018-12-09', 28],
    ['2018-12-16', 26],
    ['2018-12-23', 35],
    ['2018-12-30', 15],
    ['2019-01-06', 19],
    ['2019-01-13', 33],
    ['2019-01-20', 29],
    ['2019-01-27', 58],
    ['2019-02-03', 75],
    ['2019-02-10', 49],
    ['2019-02-17', 30],
    ['2019-02-24', 29],
    ['2019-03-03', 27],
    ['2019-03-10', 34],
    ['2019-03-17', 24],
    ['2019-03-24', 26],
    ['2019-03-31', 26],
    ['2019-04-07', 9],
    ['2019-04-14', 9],
    ['2019-04-21', 6],
    ['2019-04-28', 5],
    ['2019-05-05', 3],
    ['2019-05-12', 2],
    ['2019-05-19', 3],
    ['2019-05-26', 4],
    ['2019-06-02', 1],
    ['2019-06-09', 3],
    ['2019-06-16', 6],
    ['2019-06-23', 2],
    ['2019-06-30', 1],
    ['2019-07-07', 2],
    ['2019-07-14', 2],
    ['2019-07-21', 5],
    ['2019-07-28', 3],
    ['2019-08-04', 4],
    ['2019-08-11', 1],
    ['2019-08-18', 6],
    ['2019-08-25', 3],
    ['2019-09-01', 3],
    ['2019-09-08', 10],
    ['2019-09-15', 11],
    ['2019-09-22', 13],
    ['2019-09-29', 12],
    ['2019-10-06', 25],
    ['2019-10-13', 26],
    ['2019-10-20', 32],
    ['2019-10-27', 19],
    ['2019-11-03', 12],
    ['2019-11-10', 56],
    ['2019-11-17', 61],
    ['2019-11-24', 71],
    ['2019-12-01', 53],
    ['2019-12-08', 25],
    ['2019-12-15', 18],
    ['2019-12-22', 22],
    ['2019-12-29', 11],
    ['2020-01-05', 3]]

ts_mark_area = [
    [['2018-11-04', 14],
        ['2018-11-11', 35],
        ['2018-11-18', 39],
        ['2018-11-25', 52],
        ['2018-12-02', 37],
        ['2018-12-09', 28],
        ['2018-12-16', 26],],
    [['2019-01-20', 29],
        ['2019-01-27', 58],
        ['2019-02-03', 75],
        ['2019-02-10', 49],
        ['2019-02-17', 30],
        ['2019-02-24', 29],
        ['2019-03-03', 27],
    ],
    [
        ['2019-11-03', 12],
        ['2019-11-10', 56],
        ['2019-11-17', 61],
        ['2019-11-24', 71],
        ['2019-12-01', 53],
        ['2019-12-08', 25],
        ['2019-12-15', 18],
    ],
    [
        ['2019-09-29', 12],
        ['2019-10-06', 25],
        ['2019-10-13', 26],
        ['2019-10-20', 32],
        ['2019-10-27', 19],
    ],
    [
        ['2018-09-23', 9],
        ['2018-09-30', 17],
        ['2018-10-07', 20],
        ['2018-10-14', 27],
        ['2018-10-21', 31],
        ['2018-10-28', 25],
        ['2018-11-04', 14],
        ['2018-11-11', 35],
        ['2018-11-18', 39],
        ['2018-11-25', 52],
        ['2018-12-02', 37],
        ['2018-12-09', 28],
        ['2018-12-16', 26],
    ]
]
option = {
    title: {
        text: "Weekly purchases of Hand Sanitizer by  Males <35 ",
        textStyle: {
            fontSize: 30,
            top: 20
        },
    },
    grid: {
        left: '3%',
        right: '0%',
        top: '13%',
        bottom: '15%',
    },
    legend: {
        textStyle: {
            fontSize: 30,
            top: 20
        },
        icon: 'none'
    },
    dataZoom: {
        start: 50,
        end: 99,
        bottom: 20,
    },
    xAxis: [
        {
            position: "bottom",
            type: 'category',
            boundaryGap: false,
            nameRotate: 1,
            splitLine: {
                show: false
            },
            axisLabel: {
                show: true,
                textStyle: {
                    fontWeight: "bold",
                    fontSize: 18
                }
            }

            // data: ['Jan-2017', 'Jan-2017', 'Jan-2017', 'Feb-2017', 'Mar-2017', 'Apr-2017', 'May-2017', 'Jun-2017', 'Jul-2017', 'Aug-2017', 'Sep-2017', 'Oct-2017', 'Nov-2017', 'Dec-2017', 'Feb-2018', 'Mar-2018', 'Apr-2018', 'Mai-2018', 'Jun-2018', 'Jun-2018']
        },
        {
            position: "bottom",
            offset: 40,
            zlevel: 1,
            type: 'category',
            boundaryGap: false,
            nameRotate: 2,
            splitLine: {
                show: false
            },
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
        }
    ],
    yAxis: {
        name: "#customers",
        type: 'value'
    },
    series: [{
        data: ts_data,
        type: 'line',
        smooth: false,

    }, {
        type: "line",
        data: ts_mark_area[0],
        lineStyle: {
            width: 10,
            opacity: 0.6,
            color: 'green'
        }
    }, {
        type: "line",
        data: ts_mark_area[1],
        lineStyle: {
            width: 10,
            opacity: 0.6,
            color: 'green'
        }
    }, {
        type: "line",
        data: ts_mark_area[2],
        lineStyle: {
            width: 10,
            opacity: 0.6,
            color: 'green'
        }
    }, {
        type: "line",
        data: ts_mark_area[3],
        lineStyle: {
            width: 10,
            opacity: 0.6,
            color: 'green'
        }
    }, {
        type: "line",
        data: ts_mark_area[4],
        lineStyle: {
            width: 10,
            opacity: 0.6,
            color: 'green'
        }
    }

    ]
};

timeSeries.setOption(option);
timeSeries.resize();


$(window).on('resize', function () {
    sankeyChart.resize();
    timeSeries.resize();
});


$("#product-centric-tab").on("click", function () {
    timeSeries.setOption(option);
    timeSeries.resize();

})


// Select all options in a select
// Mouse listeners
sankeyChart.on('mouseover', (params) => {
    if (params.dataType === 'node') {
        fillDetailsTable(params.data)
    }
})


function fillDetailsTable(data) {
    let description = data.size + ", " + data.property_values + ", " + data.itemset_name.slice(1, -1)
    let period = new Date(data.period)
    period = period.toLocaleString("default", {month: 'long'}) + " " + period.getFullYear()
    $("#details-group-description").html(description)
    $("#details-group-id").html("G" + data.name)
    $("#details-group-incoming").html(data.in)
    $("#details-group-outgoing").html(data.out)
    $("#details-group-period").html(period)
}

//Smoothing for ts
$("#smoothingIterationPicker").change(function () {
    let val = $(this).val()
    options = timeSeries.getOption()
    if (val >= 1) {
        options.series[0].smooth = true
    } else {
        options.series[0].smooth = false

    }
    timeSeries.setOption(options)

})

//             itemStyle: {
//                 color: "#457b9d",
//             }
//
//         },
//         {
//             name: "Perishes",
//             type: 'bar',
//             itemStyle: {
//                 color: "#aFFFF",
//             }
//
//         },
//         {
//             "top": "0%",
//             "bottom": "-10%",
//             "left": "0%",
//             "right": "0%",
//             type: 'scatter',
//         },
//         sankey
//     ]
//     console.log("NANA")
//     sankeyChart.setOption(options)
// })
//
// $("#resultscontainer").mouseleave(function () {
//     let options = sankeyChart.getOption()
//     options["series"] = [
//         {
//             name: "Merges",
//             type: 'bar',
//             itemStyle: {
//                 color: "#e63946",
//             }
//
//         },
//         {
//             name: "Splits",
//             type: 'bar',
//             itemStyle: {
//                 color: "#1d3557",
//             }
//
//         },
//         {
//             name: "Grows",
//             type: 'bar',
//             itemStyle: {
//                 color: "#a8dadc",
//                 "opacity": 1
//
//             }
//
//
//         },
//         {
//             name: "Stable",
//             type: 'bar',
//             itemStyle: {
//                 color: "#457b9d",
//             }
//
//         },
//         {
//             name: "Perishes",
//             type: 'bar',
//             itemStyle: {
//                 color: "#aFFFF",
//             }
//
//         },
//         {
//             "top": "0%",
//             "bottom": "-10%",
//             "left": "0%",
//             "right": "0%",
//             type: 'scatter',
//         },
//         sankey_default
//     ]
//     sankeyChart.setOption(options)
// })
// ################## Query canvas
var queryCanvas = echarts.init(document.getElementById('graphquerycanvas'));
var optionquery = {
    series: [
        {
            "top": "25%",
            "bottom": "25%",
            "left": "15%",
            "right": "15%",
            "type": "sankey",
            "name": "Sankey",
            "focusNodeAdjacency": "allEdges",
            "nodeAlign": "center",
            "layout": "none",
            "data": [
                {
                    "": "0",
                    "user_ids": [
                        114932,
                        432898,
                        452425,
                        465308,
                        480726,
                        574109,
                        575523,
                        585456,
                        599789,
                        717621,
                        866133
                    ],
                    "support": "25",
                    "itemsets": "4915",
                    "period": "2017-11-01",
                    "property_values": "1",
                    "depth": 20,
                    "size": 10,
                    "sex": "1",
                    "itemset_name": "'[\"COCA COLA & CHOCOLATE BAR\"]'",
                    "name": "0",
                    "label": {
                        "normal": {
                            "distance": -1
                        }
                    },
                    "itemStyle": {
                        "z": 1,
                        "color": "rgb(27,120,0)",
                        // opacity: 0.5,
                        // borderColor: "yellow",
                        // borderType: 'dashed',
                        // borderWidth: 4,

                    },
                    "in": 0,
                    out: 2,
                },
                {
                    "": "1",
                    "user_ids": [
                        106174,
                        412666,
                        427150,
                        460243,
                        465004,
                        465308,
                        476566,
                        530327,
                        532504,
                        563195,
                        625091,
                        835363,
                        863705,
                        874591,
                        957568
                    ],
                    "support": "29",
                    "itemsets": "4112",
                    "period": "2017-12-01",
                    "property_values": "1",
                    "depth": 5882.35294117647,
                    "size": 18,
                    "sex": "1",
                    "size": 5,
                    "itemset_name": "'[\"LAVAGE CLU\"]'",
                    "name": "1",
                    "label": {
                        "normal": {
                            "distance": -1
                        }
                    },
                    "itemStyle": {
                        "z": 1,
                        "color": "rgb(27,120,0)", opacity: 1,

                    },
                    "in": 1,
                    out: 1
                },
                {
                    "": "2",
                    "user_ids": [
                        106174,
                        264679,
                        274132,
                        321135,
                        332635,
                        365367,
                        438454,
                        465004,
                        499127,
                        503579,
                        532504,
                        565442,
                        574109,
                        615324,
                        957568,
                        964386
                    ],
                    "support": "30",
                    "itemsets": "5631",
                    "period": "2017-12-01",
                    "property_values": "1",
                    "depth": 5882.35294117647,
                    "size": 19,
                    "size": 5,

                    "sex": "1",
                    "itemset_name": "'[\"TWIX 50G\"]'",
                    "name": "2",
                    "label": {
                        "normal": {
                            "distance": -1
                        }
                    },
                    "itemStyle": {
                        "z": 1,
                        "color": "rgb(27,120,0)",
                        opacity: 1

                    },
                    "in": 1,
                    "out": 2,
                },
                {
                    "": "4",
                    "user_ids": [
                        107216,
                        835363,
                        835363,
                        835363,
                        835363,
                        837950,
                        874591,
                        923982,
                        957568
                    ],
                    "support": "20",
                    "itemsets": "4112",
                    "period": "2018-02-01",
                    "property_values": "1",
                    "depth": 11764.70588235294,
                    "size": 12,
                    "size": 10,
                    "sex": "1",
                    "itemset_name": "'[\"LAVAGE CLU\"]'",
                    "name": "4",
                    "label": {
                        "normal": {
                            "distance": -1
                        }
                    },
                    "itemStyle": {
                        "z": 1,
                        "color": "rgb(27,120,0)", opacity: 1,

                    },
                    "in": 2,
                    out: 1,
                },
            ],
            "links": [
                {
                    "source": "0",
                    "target": "1",
                    "user_id": [
                        390199,
                        438114,
                        578902
                    ],
                    "value": 5,
                    "label": "S",
                    "lineStyle": {
                        "color": "#1d3557",
                        "opacity": 1
                    }
                },
                {
                    "source": "0",
                    "target": "2",
                    "user_id": [
                        114932,
                        132519,
                        332635,
                        574109
                    ],
                    "value": 5,

                    "label": "S",
                    "lineStyle": {
                        "color": "#1d3557",
                        "opacity": 1
                    }
                },
                {
                    "source": "1",
                    "target": "4",
                    "user_id": [
                        273864,
                        274953,
                        280880,
                        835363,
                        874591,
                        957568
                    ],
                    "value": 5,

                    "label": "S",
                    "lineStyle": {
                        "color": "red",
                        "opacity": 1
                    }
                },
                {
                    "source": "2",
                    "target": "4",
                    "user_id": [
                        132519
                    ],
                    "value": 5,
                    "label": "S",
                    "lineStyle": {
                        "color": "red",
                        "opacity": 1
                    }
                },
            ],
            'label': {
                distance: 0,
                position: "inside",
                formatter: ' ',
            },
        }
    ],
};
queryCanvas.setOption(optionquery)
