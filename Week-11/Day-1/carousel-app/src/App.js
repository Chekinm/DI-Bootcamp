import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import img1 from './img/honkong.jpg';
import img2 from './img/japan.webp';
import img3 from './img/lasvegas.webp';
import img4 from './img/macao.webp';



let styles = {
    margin: 'auto',
    width: '700px'
  };
  
function App() {
  return (
	<div style={styles}>
		<Carousel>
			<div style={styles}>
				<img src={img1} alt='honkong' /> 
				<p className="legend">Hong Kong</p>
			</div>
			<div>
				<img src={img2} alt="Singapore"/>
				<p className="legend">Macao</p>
			</div>
			<div>
				<img src={img3} alt="Japan"/>
				<p className="legend">Japan</p>
			</div>
			<div>
				<img src={img4} alt="Las Vegas"/>
				<p className="legend">Las Vegas</p>
			</div>
		</Carousel>
	</div>
  );
}

export default App;