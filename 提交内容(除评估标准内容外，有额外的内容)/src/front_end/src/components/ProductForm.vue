<!-- ProductForm.vue -->
<template>
  <div>
    <h1>Add Product</h1>
    <form @submit.prevent="submitForm">
      <label for="productName">Product Name:</label>
      <input type="text" v-model="productName" required>

      <label for="productPrice">Product Price:</label>
      <input type="number" v-model="productPrice" required>

      <button type="submit">Add Product</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      productName: '',
      productPrice: 0,
    };
  },

// send POST request at submitForm method
  methods: {
    submitForm() {
      // construct POST data
      const postData = {
        name: this.productName,
        price: this.productPrice,
      };

      // send POST request
      axios.post('http://127.0.0.1:8000/your_app_name/api/product-info/add', postData)
          .then(response => {
            // if request is successful, log the response data
            console.log('Product added successfully:', response.data);
            // clear the form fields
            this.productName = '';
            this.productPrice = 0;
          })
          .catch(error => {
            // otherwise, log the error
            console.error('Error adding product:', error);
          });
    },
  },

};
</script>

<style>
form {
  max-width: 300px;
  margin: auto;
}
</style>