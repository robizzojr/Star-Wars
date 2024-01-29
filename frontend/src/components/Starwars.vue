<template>
   <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Starships</h1>
        <hr><br><br>
        <select id="manufacturerSelect" @change="manufacturerSelectOnChange($event)">
          <option selected value></option>
          <option value="Kuat Drive Yards">Kuat Drive Yards</option>
          <option value="Corellian Engineering Corporation">Corellian Engineering Corporation</option>
          <option value="Feethan Ottraw Scalable Assemblies">Feethan Ottraw Scalable Assemblies</option>
        </select>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Max Speed</th>
              <th scope="col">Length</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(starship, index) in starships" :key="index">
              <td>{{ starship.name }}</td>
              <td>{{ starship.max_atmosphering_speed }}</td>
              <td>{{ starship.length }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Starwars',
  data() {
    return {
      starships: [],
    };
  },
  methods: {
    getFullListOfStarships() {
      const path = 'http://localhost:5001/starships';
      axios.get(path)
        .then((res) => {
          this.starships = res.data.starships;
        })
        .catch((error) => {

          console.error(error);
        });
    },
    manufacturerSelectOnChange(event) {
      let path = "http://localhost:5001/starships"
      const selectedManufacturer = event.target.value

      if (selectedManufacturer) {
        path = `http://localhost:5001/starships/${selectedManufacturer}`;
      }
      
      axios.get(path)
        .then((res) => {
          this.starships = res.data.starships;
          console.log(res.data)
        })
        .catch((error) => {

          console.error(error);
        });
    }
  },
  created() {
    this.getFullListOfStarships();
  },
};
</script>