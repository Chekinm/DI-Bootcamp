import React from 'react';
import './Watch.css';
import { ReactComponent as Watch } from '../svg/watch.svg';
import { ReactComponent as Minutes} from '../svg/minutes.svg';
import { ReactComponent as Hours} from '../svg/hours.svg';
import { ReactComponent as Seconds} from '../svg/seconds.svg';

const WatchSVG = (props) => {

  const rotateSecondsArrowStyle = {
    transform: `rotate(${(props.time.seconds / 60) * 360}deg)`,
  };
  const rotateMinutesArrowStyle = {
    transform: `rotate(${(props.time.minutes / 60) * 360}deg)`,
  };
  const rotateHoursArrowStyle = {
    transform: `rotate(${(props.time.hours / 12) * 360}deg)`,
  };

  return (

    <div >
      <div>{`Today is ${props.time.day}/${props.time.month}/${props.time.year}`}</div>
      <div className='watch'>
        <Watch className='dial'/>
        <Seconds className='arrow' style={rotateSecondsArrowStyle}  />
        <Minutes className='arrow' style={rotateMinutesArrowStyle} />
        <Hours   className='arrow' style={rotateHoursArrowStyle}/>
    </div>
      

      
    </div>

  );
}

export default WatchSVG;


