template_email = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, user-scalable=no">
<title>슈퍼투데이 오늘마감 리포트</title>
<style>
* {font-family:Trebuchet MS, arial, 굴림;font-size:12px;}
.main {width:960px;margin:auto;}
.main .header{background:black;color:white;padding:10px; line-height: 0;}
.main h2 {font-size:28px;font-weight:bold;}
.main h3 {font-size:20px;font-weight:bold;text-align: right;}
.main h4 {font-size:14px;font-weight:bold;text-align: center;}
td, th {padding:5px;border:solid 1px #CCCCCC;line-height:18px;}
th {background:lightgrey; font-weight:bold;}
table {border-collapse:collapse;table-layout:fixed;width:100%%;}
td{text-align:center;}
td:nth-child(3) {text-align:left}
td:nth-child(6) {text-align:right}
</style>
</head>
<body>
    <div class="main">
        <div class="header">
            <h2>슈퍼투데이 오늘마감 리포트</h2>
            <h3>%s</h3>
            <h4>*^^* 오늘도 대박나셔요. *^^*</h4>
        </div>
        <!--//////////////////////////////////////////////////////////////////-->
        %s
        <!--//////////////////////////////////////////////////////////////////-->

    </div>
</body>
</html>
'''