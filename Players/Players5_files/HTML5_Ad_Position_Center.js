var ebMainDivId = ebO.phid;
var ebAdWidth = ebO.w;
var win = window;

if(typeof(inDapIF)!='undefined' && inDapIF){
	ebMainDivId = 'ebBannerDiv_' + ebAdID + '_' + ebRand;
    win = parent;
}

function ebFixCenter() {
    var ebMainDiv = win.document.getElementById(ebMainDivId);
    if (typeof ebMainDiv !== "undefined" && ebMainDiv) {
        ebMainDiv.style.width = ebAdWidth + "px";
        ebMainDiv.style.margin = "0 auto";
        ebMainDiv.style.position = "relative";
        ebMainDiv.style.display = "block";
    } else {
        setTimeout(ebFixCenter, 500);
    }
}
ebFixCenter();