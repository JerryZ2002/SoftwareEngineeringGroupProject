<!-- PurchaseOrderComponent.vue -->

<template>

  <el-card class="box-card scrollable-card" style="width: 100%">
    <template #header>
      <div>
        <el-input v-model="searchKeyword" placeholder="输入关键字进行搜索" style="width: 60%"  />
        <el-select v-model="selectedField" placeholder="请选择搜索字段" style="width: 30%">
          <el-option v-for="field in availableFields" :key="field" :label="field" :value="field" />
        </el-select>
        <el-button type="primary" @click="searchPurchaseOrders" >搜索</el-button>
      </div>
      <div class="card-header" style="width: 90%;">
      <span>
        <el-text class="mx-1" size="large">
          商品信息
        </el-text>
      </span>
      <el-button color="#626aef" :dark="isDark" round @click="loadProductInfo()">显示所有</el-button>
      <el-button color="#626aef" :dark="isDark" round @click="addProductInfopre()">注册新商品</el-button>
      </div>
    </template>
    <el-table :data="productInformation" style="width: 90%; min-width: 800px" :max-height="400" stripe :show-header="true" :show-summary="false">
      <el-table-column prop="product_id" label="商品编号" :min-width="80"></el-table-column>
      <el-table-column prop="product_name" label="商品名称" :min-width="80"></el-table-column>
      <el-table-column prop="specification" label="规格" :min-width="80"></el-table-column>
      <el-table-column prop="description" label="描述" :min-width="80"></el-table-column>
      <el-table-column prop="classification" label="分类" :min-width="80"></el-table-column>
      <el-table-column prop="price" label="价格" :min-width="80"></el-table-column>
      <el-table-column label="操作" width="180">
        <template #default="{ row }">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <el-button type="primary" @click="editProductInfo(row)">修改</el-button>
            <el-button type="danger" @click="deleteProductInfo(row.product_id)">注销</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <template #footer>以上为所有已经注册的商品，当商品注销时相关的仓储，采购，销售记录同时清空</template>
  </el-card>


  <div>
    <div v-if="editedProduct.product_id !== null && editedProduct.product_name !== null && editedProduct.specification !== null && editedProduct.description !== null && editedProduct.classification !== null && editedProduct.price !== null && state===1">
      <h3>编辑商品信息</h3>
      <el-form @submit.prevent="updateProductInfo">

        <el-row>
          <el-col :span="8">
            <el-form-item label="商品编号" prop="product_id">
              <el-input v-model="editedProduct.product_id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="商品名称" prop="product_name">
              <el-input v-model="editedProduct.product_name" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="规格" prop="specification">
              <el-input v-model="editedProduct.specification" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="8">
            <el-form-item label="描述" prop="description">
              <el-input v-model="editedProduct.description" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="分类" prop="classification">
              <el-input v-model="editedProduct.classification" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="价格" prop="price">
              <el-input v-model="editedProduct.price" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item>
          <el-button color="#626aef" :dark="isDark" type="primary" @click="updateProductInfo">上传</el-button>
        </el-form-item>

      </el-form>
    </div>

    <div v-if="state === 2">
      <h3>注册商品信息</h3>
      <el-form @submit.prevent="addProductInfo">

        <el-row>
          <el-col :span="8">
            <el-form-item label="商品编号" prop="product_id">
              <el-input v-model="newProduct.product_id" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="商品名称" prop="product_name">
              <el-input v-model="newProduct.product_name" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="规格" prop="specification">
              <el-input v-model="newProduct.specification" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="8">
            <el-form-item label="描述" prop="description">
              <el-input v-model="newProduct.description" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="分类" prop="classification">
              <el-input v-model="newProduct.classification" type="text" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>

          <el-col :span="8">
            <el-form-item label="价格" prop="price">
              <el-input v-model="newProduct.price" type="number" :autosize="{ minRows: 1, maxRows: 4 }" required />
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item>
          <el-button color="#626aef" :dark="isDark" type="primary" @click="addProductInfo">上传</el-button>
        </el-form-item>

      </el-form>
    </div>

    <div v-if="ifadd === true">
      <h3>注册商品信息</h3>
      <el-form @submit.prevent="">
        
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
        availableFields: ["product_id", "product_name", "specification", "description", "classification", "price"],
        productInformation: [],
        ifadd : false,
        state: 0,
        newProduct: {
            product_id: null,
            product_name: null,
            specification: null,
            description: null,
            classification: null,
            price: null,
        },
        editedProduct: {
            product_id: null,
            product_name: null,
            specification: null,
            description: null,
            classification: null,
            price: null,
        },
      };
  
    },
    mounted() {
      this.loadProductInfo();
    },
    methods: {
      searchPurchaseOrders() {
      axios.get(`http://127.0.0.1:8000/your_app_name/api/product-info/search/?query=${this.searchKeyword}&field=${this.selectedField}`)
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
            this.productInformation = sortedData;
          })
          .catch(error => {
            console.error('Error:', error);
          });
      },
      loadProductInfo() {
        axios.get('http://127.0.0.1:8000/your_app_name/api/product-info/')
            .then(response => {
              this.productInformation = response.data;
              this.sortedProducts();
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      addProductInfopre() {
        // this.ifadd = !this.ifadd;
        this.ifadd = false;
        if(this.state!==2){
          this.state=2
        }
        else{
          this.state=0
        }
      },
      addProductInfo() {
        axios.post('http://127.0.0.1:8000/your_app_name/api/product-info/', this.newProduct)
            .then(response => {
            console.log('Success:', response.data);
            this.loadProductInfo();
            this.newProduct= {
                    product_id: null,
                    product_name: null,
                    specification: null,
                    description: null,
                    classification: null,
                    price: null,
            };
            // this.ifadd = !this.ifadd;
            this.ifadd = false;
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      deleteProductInfo(product_id) {
        axios.delete(`http://127.0.0.1:8000/your_app_name/api/product-info/${product_id}/`)
            .then(response => {
              if (response.status === 204) {
                console.log('Success: Purchase Order deleted');
                this.loadProductInfo();
              } else {
                console.error('Error:', response.status);
              }
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
      editProductInfo(products) {
        // load order info into the form
        this.editedProduct = { ...products };
        this.state=1;
      },
      updateProductInfo() {
        // send PATCH request to update the order
        axios.patch(`http://127.0.0.1:8000/your_app_name/api/product-info/${this.editedProduct.product_id}/`, this.editedProduct)
            .then(response => {
            console.log('Success:', response.data);
            this.loadProductInfo(); // reload the orders
            this.editedProduct = { // reset the form
                    product_id: null,
                    product_name: null,
                    specification: null,
                    description: null,
                    classification: null,
                    price: null,
                };
            })
            .catch(error => {
              console.error('Error:', error);
            });
      },
  
    },
    computed: {
      sortedProducts() {
        return this.productInformation.sort((a, b) => a.product_id - b.product_id);
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