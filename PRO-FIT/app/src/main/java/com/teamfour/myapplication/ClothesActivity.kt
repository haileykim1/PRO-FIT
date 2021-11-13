package com.teamfour.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.teamfour.myapplication.databinding.ActivityClothesBinding

class ClothesActivity : BaseActivity() {

    val binding by lazy {ActivityClothesBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
    }
}