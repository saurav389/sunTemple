let count = 0;
function addField(){
	var br = document.createElement('br');
    var container_partyname = document.getElementById("container_partyname");
    var container_itemname = document.getElementById("container_itemname");
    var container_quantity = document.getElementById("container_quantity");
    var container_rate = document.getElementById("container_rate");
    var container_amount = document.getElementById("container_amount");
    var container_date = document.getElementById("container_date");
	var partyname = document.createElement('input');
	partyname.setAttribute('type','text');
	partyname.setAttribute('name','partyname');
	partyname.style.margin = '5px';
	container_partyname.appendChild(partyname);
	partyname.appendChild(br);
	var itemname = document.createElement('input');
	itemname.setAttribute('type','text');
	itemname.setAttribute('name','itemname');
	itemname.style.margin = '5px';
	container_itemname.appendChild(itemname);
	itemname.appendChild(br);
	var quantity = document.createElement('input');
	quantity.setAttribute('type','text');
	quantity.setAttribute('name','quantity');
	quantity.setAttribute('id',`quantity${count=count+1}`);
	quantity.setAttribute('onchange','calculate(this)');
	quantity.style.margin = '5px';
	container_quantity.appendChild(quantity);
	quantity.appendChild(br);
	var rate = document.createElement('input');
	rate.setAttribute('type','text');
	rate.setAttribute('name','rate');
	rate.setAttribute('id',`rate${count}`);
	rate.setAttribute('onchange','calculate(this)');
	rate.style.margin = '5px';
	container_rate.appendChild(rate);
	rate.appendChild(br);
	var amount = document.createElement('input');
	amount.setAttribute('type','text');
	amount.setAttribute('name','amount');
	amount.setAttribute('id',`amount${count}`);
	amount.style.margin = '5px';
	container_amount.appendChild(amount);
	amount.appendChild(br);
	var date = document.createElement('input');
	date.setAttribute('type','date');
	date.setAttribute('name','date');
	date.style.margin = '5px';
	container_date.appendChild(date);
	date.appendChild(br);

}

function calculate(quantity){
    var qt = document.getElementById(quantity.id);
    if(quantity.name=='quantity'){
    	var rateid = `rate${quantity.id}`.replace('quantity','');
    	var amtid = `amount${quantity.id}`.replace('quantity','')
    	var qtid = `quantity${quantity.id}`.replace('quantity','');
    }
    else{
    	var rateid = `rate${quantity.id}`.replace('rate','');
    	var amtid = `amount${quantity.id}`.replace('rate','');
    	var qtid = `quantity${quantity.id}`.replace('rate','');
    }
    var rate = document.getElementById(rateid);
    var qtv = document.getElementById(qtid);
    var amount = document.getElementById(amtid);

    var amnt = Number(qtv.value)*Number(rate.value);
    amount.value = amnt;

}
