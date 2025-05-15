// src/api.js
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const addStudyLog = (logData) => {
  return axios.post(`${API_BASE_URL}/studylogs/`, logData);
};

export const getStudyLogs = () => {
  return axios.get(`${API_BASE_URL}/studylogs/`);
};
