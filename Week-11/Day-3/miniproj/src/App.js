import React, { Fragment } from 'react';

import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

import { ColumnLeft } from './columns/ColumnLeft';
import { ColumnRight } from './columns/ColumnRight';



export const App = () => {
  return (
    <Fragment>
      <Navbar >
        <Navbar.Brand>Error boundaries in react</Navbar.Brand>
      </Navbar>

      <Container fluid>
        <Row>
          <Col >
            <ColumnLeft />
          </Col>

          <Col>
          
            <ColumnRight />
          
          </Col>
        </Row>
      </Container>
    </Fragment>
  );
};
