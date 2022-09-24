/* 
This helps you to collect specific column values.
I needed this when the attacker change IP with subnetting IPs.
We don't have permission to block a subnet collectively instead we can block each IP separately.
*/

// This helps you to collect specific column values.
// Soar has a dynamic naming feature therefore you need to change the str variable. 
// To specify the range you need to use the FortiSoar search feature with the for loop integer range.
const ips = [];
for (let i = 0; i < 50; i++) {

   var str="#\\31 663971055304-"+i+"-uiGrid-000C-cell > div";
   var b=document.querySelector(str).innerText;
   console.log(b);
   ips.push(b);
  
}
console.log(ips);
