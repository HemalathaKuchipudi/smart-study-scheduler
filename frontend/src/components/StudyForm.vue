   <template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-tr from-blue-200 via-indigo-200 to-purple-200 px-4">
    <div class="w-full max-w-xl bg-white/90 backdrop-blur-md p-10 rounded-3xl shadow-xl">
      <h1 class="text-3xl font-bold text-center text-purple-800 mb-8">📘 Add Study Log</h1>

      <form @submit.prevent="submitLog" class="space-y-12">
        <div>
          <label class="block text-gray-700 text-sm font-medium mb-1">Topic</label>
          <input
            v-model="topic"
            type="text"
            class="w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500"
            placeholder="e.g. Data Structures"
            required
          />
        </div>

        <div>
          <label class="block text-gray-700 text-sm font-medium mb-1">Date Studied</label>
          <input
            v-model="dateStudied"
            type="date"
            class="w-full px-4 py-3 rounded-xl border border-purple-300 focus:outline-none focus:ring-2 focus:ring-purple-500"
            required
          />
        </div>

        <div class="mt-8">
          <button
            type="submit"
            class="w-full bg-purple-600 text-white py-3 rounded-xl text-lg font-semibold hover:bg-purple-700 transition"
          >
            ➕ Submit
          </button>
        </div>
      </form>

      <div v-if="studyLogs.length" class="mt-10">
        <h2 class="text-xl font-semibold text-purple-800 mb-4">📅 Your Study Logs</h2>
        <ul class="space-y-4">
          <li
            v-for="log in studyLogs"
            :key="log.id"
            class="bg-white p-4 rounded-xl shadow border-l-4 border-purple-500"
          >
            <p class="text-gray-800"><strong>Topic:</strong> {{ log.topic }}</p>
            <p class="text-gray-800"><strong>Date Studied:</strong> {{ log.date_studied }}</p>
            <p class="text-gray-800"><strong>Next Review:</strong> {{ log.next_review_date }}</p>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'StudyForm',
  data() {
    return {
      topic: '',
      dateStudied: '',
      studyLogs: []
    };
  },
  mounted() {
    this.fetchLogs();
  },
  methods: {
    async fetchLogs() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/studylogs/');
        this.studyLogs = response.data;
      } catch (err) {
        console.error('Failed to fetch logs:', err);
      }
    },
    async submitLog() {
      try {
        const payload = {
          topic: this.topic,
          date_studied: this.dateStudied
        };
        await axios.post('http://127.0.0.1:8000/studylogs/', payload);
        this.topic = '';
        this.dateStudied = '';
        this.fetchLogs();
      } catch (err) {
        console.error('Failed to submit:', err);
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}
</style>
