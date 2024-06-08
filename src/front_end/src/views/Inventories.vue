<!-- PurchaseOrderComponent.vue -->

<template>
  <el-card class="box-card scrollable-card" style="width: 100%">
    <template #header>
      <div class="card-header" style="width: 90%;">
      <span>
        <el-text class="mx-1" size="large">
          库存
        </el-text>
      </span>
      </div>
    </template>
    <el-table :data="IventoryInformation" style="width: 90%; min-width: 800px" :max-height="400" stripe :show-header="true" :show-summary="false">
      <el-table-column prop="product_id" label="商品编号" :min-width="80"></el-table-column>
      <el-table-column prop="stock_quantity" label="仓储量" :min-width="80"></el-table-column>
      <el-table-column label="操作" width="180">
        <template #default="{ row }">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            
            <el-button type="primary" @click="editIventoryInfo(row)">修改</el-button>
            <div v-if=" row.stock_quantity < 100 && row.stock_quantity > 10"><el-button style="width: 60px" type="warning">Warning</el-button></div>
            <div v-if=" row.stock_quantity <= 10"><el-button style="width: 60px" type="danger">Danger</el-button></div>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <template #footer>以上为所有已经注册的商品的仓储量，为0表示仓库暂时没有该商品，当商品注销时仓储记录同时清空，当商品数量介于10-100会黄色预警，数量少于10个会红色预警</template>
  </el-card>


  <div>
      <!-- 编辑表单 -->
      <div v-if="editedIventory.product_id !== null && editedIventory.stock_quantity !== null">
        <h3>编辑仓储信息</h3>
        <el-form>
          <label for="edited product_id">商品编号：</label>
          <el-input v-model="editedIventory.product_id" id="edited product_id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />

          <label for="edited stock_quantity">仓储：</label>
          <el-input v-model="editedIventory.stock_quantity" id="edited stock_quantity" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />

          <el-button color="#626aef" :dark="isDark" type="primary" @click="updateIventoryInfo" >上传</el-button>
        </el-form>
      </div>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        searchKeyword : "",
        selectedField: null,
        availableFields: ["stock_quantity"],
        IventoryInformation: [],
        newIventory: {
            product_id: null,
            stock_quantity: null,
        },
        editedIventory: {
            product_id: null,
            stock_quantity: null,
        },
      };
  
    },
    mounted() {
      this.loadIventories();
    },
    methods: {
      searchPurchaseOrders() {
      axios.get(`http://127.0.0.1:8000/your_app_name/api/inventories/search/?query=${this.searchKeyword}&field=${this.selectedField}`)
          .then(response => {
            const sortedData = response.data.sort((a, b) => {
              if (new Date(a.purchase_date) < new Date(b.purchase_date)) {
                return -1;
              } else if (new Date(a.purchase_date) > new Date(b.purchase_date)) {
                return 1;
              } else {
                if (a.order_number < b.order_number) {
                  return -1;
                } else {
                  return 1;
                }
              }
            });
            this.IventoryInformation = sortedData;
          })
          .catch(error => {
            console.error('Error:', error);
          });
      },
      loadIventories() {
        axios.get('http://127.0.0.1:8000/your_app_name/api/inventories/')
            .then(response => {
              this.IventoryInformation = response.data;
              this.sortedProducts();
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      addPurchaseOrder() {
        axios.post('http://127.0.0.1:8000/your_app_name/api/inventories/', this.newIventory)
            .then(response => {
            console.log('Success:', response.data);
            this.loadIventories();
            this.newIventory= {
                  product_id: null,
                  stock_quantity: null,
                };
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      deleteIventoryInfo(product_id) {
        axios.delete(`http://127.0.0.1:8000/your_app_name/api/inventories/${product_id}/`)
            .then(response => {
              if (response.status === 204) {
                console.log('Success: Purchase Order deleted');
                this.loadIventories();
              } else {
                console.error('Error:', response.status);
              }
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      editIventoryInfo(inventories) {
        // load order info into the form
        this.editedIventory = { ...inventories };
      },
      updateIventoryInfo() {
        // send PATCH request to update the order
        axios.patch(`http://127.0.0.1:8000/your_app_name/api/inventories/${this.editedIventory.product_id}/`, this.editedIventory)
            .then(response => {
            console.log('Success:', response.data);
            this.loadIventories(); // reload the orders
            this.editedIventory = { // reset the form
                  product_id: null,
                  stock_quantity: null,
                };
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
  
    },
    computed: {
      sortedProducts() {
        return this.IventoryInformation.sort((a, b) => a.product_id - b.product_id);
      },
    },
  };
</script>

<style>  
  .card-header {  
    display: flex;  
    justify-content: space-between;  
    align-items: center;  
  }  
      
  .text {  
    font-size: 14px;  
  }  
      
  .item {  
    margin-bottom: 18px;  
  }  
      
  .box-card {
  width: 800px;
  height: 630px;
}
      
  .scrollable-card {  
    overflow: auto;
  }  
  </style>