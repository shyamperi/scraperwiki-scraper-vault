<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>UK party donations latest</title>
    <style type="text/css" media="screen">
        p{padding:1px;}
        table.out { border-collapse: collapse; border: 1 }
        table.out th { background-color :black; color:white; border-left: thin white solid; border-right: thin white solid }
        table.out td { border: thin black solid }
        #qidout, #qidrec { background:#eef; }
    </style>
    <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
    <script type="text/javascript" src="http://media.scraperwiki.com/js/json-min.js"></script>
</head>

<body>

<p>This feeds off the scraper <a href="http://scraperwiki.com/scrapers/cabinet_office_spend_data/">Cabinet Office Spend Data</a>.
This data is originally sourced from <a href="http://www.cabinetoffice.gov.uk/resource-library/cabinet-office-spend-data">this page</a></p>

<h2>Top 10 Receivers of Cabinet Office Money</h2>
<div id="idrec"></div>


<script>
function addCommas(el)
{
    if (typeof el != 'number')
        return el; 
    var nStr = el.toFixed(2); 
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}

function puttable(idd, result)
{
    var keys = result.keys;
    var data = result.data;
    $(idd).html('<table class="out"></table>');
    $(idd+" table").append($("<tr><th>"+keys.join("</th><th>")+"</th></tr>"));
    for (var i = 0; i < data.length; i++)
    {
        data[i][1] = addCommas(data[i][1]); 
        $(idd+" table").append($('<tr><td class="col1">'+data[i].join("</td><td>")+"</td></tr>"));
    }
}


$(document).ready(function()
{
    var src = "cabinet_office_spend_data";
    var apiurl = "http://api.scraperwiki.com/api/1.0/datastore/sqlite";            
    var sqlselect = "SELECT Supplier, sum(Amount) as Total FROM Refined GROUP BY Supplier ORDER BY sum(Amount) desc LIMIT 10";
    $.ajax({url:apiurl, dataType:"jsonp", data:{name:src, query:sqlselect, format:"jsonlist"}, success:function(tdata)
    {
        puttable("#idrec", tdata); 
    }}); 

});
</script>

</body>
</html>


