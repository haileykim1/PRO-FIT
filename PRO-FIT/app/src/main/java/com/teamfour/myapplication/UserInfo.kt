package com.teamfour.myapplication

import android.app.Application
import android.content.Context
import android.content.Context.MODE_PRIVATE
import android.content.SharedPreferences
import android.provider.Settings.Global.getString

class UserInfo() {
    companion object{
        val context = MyApplication.ApplicationContext()
        val sharedPref = context?.getSharedPreferences(
            context.getString(R.string.preference_file_key), Context.MODE_PRIVATE
        )
        const val NAME = "name"
        const val NAME_PASSED = "name_passed"
        const val DEFAULT_NAME = "DEFAULT"

    }
/*
    val sharedPref = context?.getSharedPreferences(
        context.getString(R.string.preference_file_key), Context.MODE_PRIVATE
    )*/





    fun has(key: String): Boolean {
        val value = sharedPref.getString(key, null)
        if(value != null){
            return true
        }
        return false
    }

    fun get(key: String):Any? {
        return sharedPref.getString(key, null)
    }

    fun set(key: String, value: String){
        with(sharedPref.edit()){
            putString(key, value)
            commit()
        }
    }

}