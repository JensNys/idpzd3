
async function draw(){



  
  const data = await d3.json("example.json");
  
  // data = {svg:{id:0,width:800,height:400},
  //   circles:[{id:1, r: 40,cx:50,cy:50,color:"red"},
  //     {id:2, r: 40,cx:150,cy:50,color:"blue"},
  //     {id:3, r: 40,cx:150,cy:150,color:"yellow"},
  // ],links:[
  //     {id:4,from:1,to:2,color:"black"},
  //     {id:5,from:2,to:3,color:"black"}
  // ],rects:[{id:6,x:300,y:50,width:100,height:200,color:"blue"}]}
  
  let svg = d3.selectAll('svg')//.append("p").text("boe");
  .data([data.svg])
  .join("svg")
  .attr('width', d=>d?.width ?? 600)
  .attr('height',d=>d?.height ?? 300)
  .attr('id',d=>d?.id ?? 0),
  margin = { top: 50, right: 50, bottom: 50, left: 50 };

  
  
  
  
  
  //de gewone lookup geeft een lijst terug, maar gezien id uniek is krijgen we singleton lijsten. Daarom nog [0]
  const id_to_circle = d3.rollup(data.circles,e=>e[0],d=>d.id)
  
  svg.selectAll("line")
  .data(data.links)
  .join("line")
  .attr("x1", d => id_to_circle.get(d.from)?.cx ?? 0)
  .attr("y1", d => id_to_circle.get(d.from)?.cy ?? 0)
  .attr("x2", d => id_to_circle.get(d.to)?.cx ?? 0)
  .attr("y2", d => id_to_circle.get(d.to)?.cy ?? 0)
  .attr("stroke", d => d.color ?? "black")
  .attr('stroke-width',5)
  ;

  
  svg.selectAll("circle")
      .data(data.circles)
      .join("circle")
      .attr("cx", d => d.cx)
      .attr("cy", d => d.cy)
      .attr("r", d => d.r)
      .attr("fill",d=>d.color)
      .attr('stroke','black');


  
  svg.selectAll("rect")
      .data(data.rects)
      .join("rect")
      .attr('x', d=>d.x)
      .attr('y', d=>d.y)
      .attr('width', d=>d.width)
      .attr('height', d=>d.height)
      .attr('fill', d=>d.color)
      .attr('stroke','black');
}



draw();

