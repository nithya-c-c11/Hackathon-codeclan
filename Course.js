// src/components/Course.js
import React from 'react';

const Course = ({ name, type, teacher }) => {
  return (
    <div className="course">
      <h4>{name}</h4>
      <p>Type: {type}</p>
      <p>Teacher: {teacher}</p>
    </div>
  );
};

export default Course;
