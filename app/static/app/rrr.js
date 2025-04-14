console.log("aaaaaaaaaa");
const home=document.getElementById("home");
const loan=document.getElementById("lean");
const settings=document.getElementById("settings");
const historyy=document.getElementById("history")
const logout=document.getElementById("logout");
const list=[home,loan,settings,historyy,logout];
function change(event)
{
    for (let j=0;j<list.length;j++)
    {
        list[j].style.backgroundColor="rgb(230, 230, 230)";
    }
    event.target.style.backgroundColor="rgb(190, 190, 190)";
}
for(let i=0;i<list.length;i++)
{
    list[i].addEventListener("click",change);
}