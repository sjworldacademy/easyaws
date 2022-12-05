template_email = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, user-scalable=no">
<title>일일 리포트</title>
<style>
* {font-family:Trebuchet MS, arial, 굴림;font-size:12px;}
.main {width:960px;margin:auto;}
td, th {padding:5px;border:solid 1px #CCCCCC;line-height:18px;}
th {background:lightgrey; font-weight:bold;}
table {border-collapse:collapse;table-layout:fixed;width:100%%;}
</style>
</head>
<body>
    <div class="main">
        <table border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td style="background-color:#4F5258;">
                    <div style="padding:10px 0 10px 15px;color:#FFFFFF;">
                        <font style="font-size:20px;font-weight:bold;">신탁사이트 일일 리포트</font>
                    </div>
                    <div style="float:right;padding:10px 10px 10px 15px;color:#FFFFFF;">
                        <font style="font-size:14px;font-weight:bold;">%s</font>
                    </div>
                </td>
            </tr>
        </table>

        <div style="width:100%%;margin-left:5px;padding-top:10px;line-height:17px;">
            <br>오늘도 대박나셔요. *^^*
        </div>

        %s

    </div>
</body>
</html>
'''