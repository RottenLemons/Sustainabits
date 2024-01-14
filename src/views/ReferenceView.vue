<template>
  <div class="flex flex-column justify-content-center" style="width: 100%; height:92vh; background-color: #a3b18a; opacity: 0.8; background-image: radial-gradient(circle at 0 0, #3a5a40, #a3b18a), repeating-radial-gradient(circle at 0 0, #3a5a40, #3a5a40, 40px, transparent 80px, transparent 40px); background-blend-mode: multiply;">
      <div class="flex flex-column justify-content-center align-items-center" style="margin-top: 3em;">
          <p style="font-size: 4em; font-weight: bold; color: white; margin-top:0;">
          References
          </p>

          <DataTable showGridlines :value="webs" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" style="width: 85%">
              <Column field="website" header="Website" sortable style="width: 35%"></Column>
              <Column field="reason" header="Reason" sortable style="width: 65%"></Column>
          </DataTable>
      </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Web } from '@/service/Web';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

onMounted(() => {
  Web.getWebs().then((data) => (webs.value = data));
});

const webs = ref();

</script>

