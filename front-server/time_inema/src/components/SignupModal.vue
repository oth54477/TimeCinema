<template>
  <transition name="modal" appear>
    <div class="modal modal-overlay" @click.self="$emit('close')">
      <div class="modal-window">
        <div class="modal-content">
          <SignUp />
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import SignUp from '@/components/SignUp'

export default {
  name: 'SignuplModal',
  props: {
  },
  components: {
    SignUp,
  },
}
</script>

<style scoped lang="stylus">
.modal {
  &.modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 33;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }

  &-window {
    background: #201f1f;
    border-radius: 4px;
    overflow: hidden;
    width: 70%;
  }

  &-content {
    padding: 10px 20px;
    padding 0px
    overflow-y: auto;
  }

  &-footer {
    background: #ccc;
    padding: 10px;
    text-align: right;
  }
}

// 오버레이 트랜지션
.modal-enter-active, {
  transition: opacity 2.5s;

  // 오버레이에 포함되어 있는 모달 윈도의 트랜지션
  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

.modal-leave-active {
  transition: opacity 1.5s;

  // 오버레이에 포함되어 있는 모달 윈도의 트랜지션
  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

// 딜레이가 적용된 모달 윈도가 제거된 후에 오버레이가 사라짐


.modal-enter, .modal-leave-to {
  opacity: 0;
}
</style>