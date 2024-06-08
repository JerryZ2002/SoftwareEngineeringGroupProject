<!-- ProductList.vue -->
<template>
  <div>
    <h1>Product List</h1>
    <ul>
      <li v-for="product in products" :key="product.id">
        {{ product.name }} - ${{ product.price }}
        <button @click="deleteProduct(product.id)">Delete</button>
        <button @click="editProduct(product)">Edit</button>
      </li>
    </ul>
    <div v-if="editingProduct">
      <h2>Edit Product</h2>
      <form @submit.prevent="submitEditForm">
        <label for="editProductName">Product Name:</label>
        <input type="text" v-model="editProductName" required>

        <label for="editProductPrice">Product Price:</label>
        <input type="number" v-model="editProductPrice" required>

        <button type="submit">Save Changes</button>
        <button @click="cancelEdit">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [],
      editingProduct: null,
      editProductName: '',
      editProductPrice: 0,
    };
  },
  mounted() {
    // Fetch products when the component is mounted
    this.fetchProducts();
  },
  methods: {

    editProduct(product) {
      // Set the editingProduct to the selected product
      this.editingProduct = product;
      // Set the initial values for the form fields
      this.editProductName = product.name;
      this.editProductPrice = product.price;
    },
    cancelEdit() {
      // Clear the editingProduct and form fields
      this.editingProduct = null;
      this.editProductName = '';
      this.editProductPrice = 0;
    },
    async submitEditForm() {
      try {
        // Update the product on the server
        await axios.put(`http://127.0.0.1:8000/your_app_name/api/product-info/${this.editingProduct.id}/update/`, {
          name: this.editProductName,
          price: this.editProductPrice,
        });

        // Refresh the product list
        await this.fetchProducts();
        // Clear the editingProduct and form fields
        this.cancelEdit();
      } catch (error) {
        console.error('Error updating product:', error);
      }
    },
    deleteProduct(productId) {
      // send DELETE request to the server
      axios.delete(`http://127.0.0.1:8000/your_app_name/api/product-info/${productId}`)
          .then(() => {
            // success message
            console.log('Product deleted successfully');
            // refresh the product list
            this.fetchProducts();
          })
          .catch(error => {
            console.error('Error deleting product:', error);
          });
    },
    async fetchProducts() {
      // use Axios or Fetch API to fetch products from the server
      // there are many ways to do this, here is one example using Axios: /api/products
      try {
        const response = await axios.get('http://127.0.0.1:8000/your_app_name/api/product-info');
        this.products = response.data;
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
  },
};
</script>

<style>
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 10px;
}
</style>

