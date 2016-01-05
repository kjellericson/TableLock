#!/usr/bin/perl
#
# This is the private generator for Kjell's page.
# It generates my web output.  Use the index.html instead.
#
#


require "/home/kjer/public_html/inc/header.pm";
use CGI;

print CGI::header();

print "<html><head><title>TableLock - freeze panes, lock headers in HTML</title>\n";
print qq(
<script type='text/javascript' src='TableLock.js'></script>
<script>
	 function tablelock_onload()
	 {
	     TableLock("mytable_t1", "rowclass_t1", "colclass_t1", "lockclass_t1");
	     TableLock("mytable_t2", "rowclass_t2", "colclass_t2", "lockclass_t2");
	 }
	 window.addEventListener("load", tablelock_onload);
</script>
);

print get_menu();
print show_banner();

print "<h1 id=logo>TableLock example</h1>\n";

$help = qq(<table id='table_class_name'>
  <tr>
    <td class='locked_class_name'>Upper left is moving both wayslocked</td>
    <td class='column_class_name'>column 1</td>
    <td class='column_class_name'>column 2</td>
    <td class='column_class_name'>column 3</td>
  </tr>
  <tr>
    <td class='row_class_name'>row 1</td>
    <td>data 1</td>
    <td>data 2</td>
    <td>data 3</td>
  </tr>
  <tr>
    <td class='row_class_name'>row 2</td>
    <td>data 1</td>
    <td>data 2</td>
    <td>data 3</td>
  </tr>
</table>
)
    ;
$help =~ s/</&lt;/g;
$help =~ s/>/&gt;/g;

my $cols = 20;
my $rows = 30;

print qq(
<b>Updated 2016-01-05</b>
<p>
Below you will have two tables with $cols columns and $rows rows.<br>
When you scroll the content in your browser the headline or linedescription are freezed.
<p>
The script uses classes for defining what parts to use for scrolling.
You shall mark the things:

<ul>
<li> One id for the table.
<li> One class name for to row cells to lock
<li> One class name for the column cells to lock
<li> The upper left cell that moves both ways (I call it "locked").
</ul>

Set a field to <i>null</i> in order to skip that part.

You init the function by calling:
<pre>
  TableLock("table_class_name", "row_class_name", "column_class_name", "locked_class_name");
</pre>

The table is made up like this:
<pre>$help</pre>
<p>
Download script here: <a href='TableLock.js'>TableLock.js</a>.
)
;

make_table("t1");
make_table("t2");


print "<div class=\"noprint\">\n";
print get_guestbook_form();
print "</div>\n";
print get_footer();


sub make_table
{
    my ($name) = @_;
    print "<h2>Table $name</h2>\n";
    print "<table id='mytable_$name' border=2 cellpadding=2>";
    print "<tr style='border:1px solid black'>";
    print "<td style='background:cyan' class='lockclass_$name'>locked</td>";
    print "<td style='background:cyan' class='lockclass_$name'>lock</td>";
    for my $col (1..$cols) {
        print "<TH style='background:grey' class='colclass_$name'>$name-row - $col</th>";
    }
    print "</tr>\n";
    
    for my $row (1..$rows) {
        print "<tr>";
        print "<td class='rowclass_$name' style='background:yellow; border-left:1px solid black'>Row $row</td>";
        print "<td class='rowclass_$name' style='background:yellow; border-right:1px solid black'>Row $row+1</td>";
        for my $col (1..$cols) {
            print "<td style='background:green'>Example&nbsp;text&nbsp;in table $name row $row, col $col</td>";
        }
        print "</tr>\n";
    }
    print "</table>\n";
}
