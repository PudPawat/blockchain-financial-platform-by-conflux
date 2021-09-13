db
    .collection("section2")
    .orderBy("createdAt","desc")
    .get()
    .then(function(collection){ // success
        console.log("get Data!",collection)
        //loop
        collection.forEach(function(doc){
            // console.log("doc",doc)
            var product =doc.data();
            console.log("product",product)
            var col =`
                <div class="col-md-4">
                    <div class ="card mb-3">
                        <img src="${product.thum}" class="card-img-top"> 
                        <div class ="card-body">
                            <h4>${product.name}</h4>
                            <h4>${product.sub}</h4>
                        </div>
                    </div> 
                </div>`;
            $("#section2").append(col)
        })
    })
    .catch(function(collection){ // fail
        console.log("[error]:",err)
    })

// 網頁的主程式寫在這裡
// .ad-toggle-btn click event
$(".ad-toggle-btn").click(function () {
    console.log('[.ad-toggle-btn被點擊了]');

});

// .navbar .nav-link click event
$(".navbar .nav-link").click(function () {
    console.log('[nav-link was clicked]', this)
    // Get the scrolling target for this anchor tag(this)
    var target = $(this).attr("href")
    console.log("[target]", target)
    // Get the position of the target
    var position = $(target).offset().top
    console.log("[position]", position);
    // Set animation time for scrolling
    var duration = 500;
    // Run scrolling animation
    // .animate( JavaScriptObject{}, duration )
    $("html,body").animate({
        scrollTop: position
    }, duration)
});


// TODO: id="createProductForm" submit event
$("#createWorkForm").submit(function(event){
    event.preventDefault();
    // event.preventDefault(): prevent the browser to refresh the page
    console.log("Form Submitted")
    var product ={
        name:$("#todoTitle").val(),
        sub:$("#todoSub").val(),
        thum:$("#todoThum").val(),
        createdAt: new Date()
    }
    console.log("[product]",product)

    //cloud firestone: save our product to database
    db.collection("section2")
    .add(product)
    .then(function(){ // success
        alert("Product Created!")
    })
    .catch(function(){ // fail
        console.log("[error]:",err)
        alert("Product Fail!")
    })
})


