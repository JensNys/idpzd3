
async function draw(){



  
  //const data = await d3.json("example.json");
  //
  data = {svg:{id:0,width:800,height:300},
    circles:[{id:1, r: 40,cx:50,cy:50,color:"red"},
      {id:2, r: 40,cx:150,cy:50,color:"blue"},
      {id:3, r: 40,cx:150,cy:150,color:"yellow"},
  ],links:[
      {id:4,from:1,to:2,color:"black"},
      {id:5,from:2,to:3,color:"black"}
  ]}
  
  let svg = d3.select('body')//.append("p").text("boe");
  .append("svg")
  .attr('width', 600)
  .attr('height', 300)
  .attr('id',0),
  margin = { top: 50, right: 50, bottom: 50, left: 50 };

  
  
  
  
  
  //de gewone lookup geeft een lijst terug, maar gezien id uniek is krijgen we singleton lijsten. Daarom nog [0]
  const id_to_circle = d3.rollup(data.circles,e=>e[0],d=>d.id)
  
  svg.selectAll("line")
      .data(data.links)
      .join("line")
      .attr("x1", d => (id_to_circle.get(d.from).cx))
      .attr("y1", d => id_to_circle.get(d.from).cy)
      .attr("x2", d => id_to_circle.get(d.to).cx)
      .attr("y2", d => id_to_circle.get(d.to).cy)
      .attr("stroke",d=>d.color);
  
  svg.selectAll("circle")
      .data(data.circles)
      .join("circle")
      .attr("cx", d => d.cx)
      .attr("cy", d => d.cy)
      .attr("r", d => d.r)
      .attr("fill",d=>d.color);
}

draw();

